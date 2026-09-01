#!/usr/bin/env python3
"""Quantify expected-versus-measured foot contacts in a ROS 2 bag."""

import argparse
import csv
import json
from pathlib import Path

from rclpy.serialization import deserialize_message
from rosbag2_py import ConverterOptions, SequentialReader, StorageOptions
from rosidl_runtime_py.utilities import get_message


LEGS = ('fl', 'fr', 'rl', 'rr')


def open_reader(path):
    reader = SequentialReader()
    reader.open(
        StorageOptions(uri=str(path), storage_id='sqlite3'),
        ConverterOptions(input_serialization_format='cdr',
                         output_serialization_format='cdr'))
    types = {item.name: item.type for item in reader.get_all_topics_and_types()}
    return reader, types


def read_window(path, allow_open_window=False):
    reader, types = open_reader(path)
    commands = []
    final_stamp = None
    while reader.has_next():
        topic, raw, stamp = reader.read_next()
        final_stamp = stamp
        if topic == '/nova/gait_command':
            msg = deserialize_message(raw, get_message(types[topic]))
            commands.append((stamp, msg.data))
    starts = [(stamp, command) for stamp, command in commands
              if command in ('gateo', 'crawl', 'paso', 'step')]
    if not starts:
        raise RuntimeError('No hay marcador gateo/crawl/paso/step')
    start, start_command = max(starts)
    stop = next((stamp for stamp, command in commands
                 if stamp > start and command in ('stand', 'stop')), None)
    if stop is None:
        if not allow_open_window or final_stamp is None:
            raise RuntimeError('No hay marcador stand/stop posterior')
        stop = final_stamp + 1
    mode = 'crawl' if start_command in ('gateo', 'crawl') else 'step'
    return start, stop, commands, mode


def diagnostic_state(data):
    """Return expected, filtered and raw contact tuples.

    Bags recorded before raw contact was added remain analyzable: their raw
    tuple is ``None`` and only the historical filtered/observed result is
    reported.
    """
    expected = tuple(leg in data.get('expected_contacts', []) for leg in LEGS)
    filtered_names = data.get(
        'filtered_observed_contacts', data.get('observed_contacts', []))
    filtered = tuple(leg in filtered_names for leg in LEGS)
    raw_names = data.get('raw_observed_contacts')
    raw = (tuple(leg in raw_names for leg in LEGS)
           if raw_names is not None else None)
    return expected, filtered, raw


def read_states(path, start, stop, mode):
    reader, types = open_reader(path)
    states = []
    phases = []
    while reader.has_next():
        topic, raw, stamp = reader.read_next()
        if stamp < start or stamp >= stop:
            continue
        if topic not in ('/nova/contact_diagnostics', '/nova/gait_phase'):
            continue
        msg = deserialize_message(raw, get_message(types[topic]))
        data = json.loads(msg.data)
        if topic == '/nova/gait_phase':
            if data.get('mode') == mode:
                phases.append((stamp, data))
            continue
        if (data.get('mode') != mode
                or not data.get('contact_plan_available', False)):
            continue
        state = diagnostic_state(data)
        if not states or state != states[-1][1]:
            states.append((stamp, state))
    return states, phases


def complete_cycles(phases, samples_per_cycle):
    samples = {}
    for _, phase in phases:
        samples.setdefault(int(phase['cycle_index']), set()).add(
            int(phase['sample_index']))
    return sorted(cycle for cycle, indexes in samples.items()
                  if indexes == set(range(samples_per_cycle)))


def transition_events(states, component):
    events = {leg: [] for leg in LEGS}
    if not states:
        return events
    previous = states[0][1][component]
    for stamp, state in states[1:]:
        current = state[component]
        for index, leg in enumerate(LEGS):
            if current[index] != previous[index]:
                events[leg].append((stamp, current[index]))
        previous = current
    return events


def states_with_component(states, component):
    """Drop samples where an optional contact representation is unavailable."""
    return [(stamp, (state[0], state[component])) for stamp, state in states
            if state[component] is not None]


def pair_transitions(expected_events, observed_events, max_delta_ns=1_800_000_000):
    rows = []
    used = set()
    for expected_stamp, target in expected_events:
        candidates = [(abs(observed_stamp - expected_stamp), index, observed_stamp)
                      for index, (observed_stamp, observed_target)
                      in enumerate(observed_events)
                      if index not in used and observed_target == target
                      and abs(observed_stamp - expected_stamp) <= max_delta_ns]
        if not candidates:
            rows.append((expected_stamp, target, None, None))
            continue
        _, index, observed_stamp = min(candidates)
        used.add(index)
        rows.append((expected_stamp, target, observed_stamp,
                     (observed_stamp - expected_stamp) / 1e9))
    return rows


def agreement(states, start, stop):
    totals = {leg: 0.0 for leg in LEGS}
    matches = {leg: 0.0 for leg in LEGS}
    all_match = 0.0
    for index, (stamp, (expected, observed)) in enumerate(states):
        end = states[index + 1][0] if index + 1 < len(states) else stop
        duration = max(0.0, (end - max(stamp, start)) / 1e9)
        if expected == observed:
            all_match += duration
        for leg_index, leg in enumerate(LEGS):
            totals[leg] += duration
            if expected[leg_index] == observed[leg_index]:
                matches[leg] += duration
    total = sum(totals.values()) / len(LEGS) if totals else 0.0
    return total, all_match, totals, matches


def write_csv(path, rows):
    fields = ['leg', 'transition', 'expected_time_s', 'observed_time_s',
              'delay_s', 'paired']
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def transition_analysis(states, start):
    expected_events = transition_events(states, 0)
    observed_events = transition_events(states, 1)
    rows = []
    summary = {}
    for leg in LEGS:
        pairs = pair_transitions(expected_events[leg], observed_events[leg])
        for expected_stamp, target, observed_stamp, delay in pairs:
            rows.append({
                'leg': leg,
                'transition': 'landing' if target else 'liftoff',
                'expected_time_s': (expected_stamp - start) / 1e9,
                'observed_time_s': (observed_stamp - start) / 1e9
                if observed_stamp is not None else '',
                'delay_s': delay if delay is not None else '',
                'paired': observed_stamp is not None,
            })
        for name, target in (('liftoff', False), ('landing', True)):
            summary[(leg, name)] = [
                delay for _, paired_target, _, delay in pairs
                if paired_target == target and delay is not None]
    return rows, summary


def contact_loss_episodes(states, stop):
    """Measure bounded false intervals for each observed contact tuple."""
    episodes = {leg: [] for leg in LEGS}
    starts = {leg: None for leg in LEGS}
    for stamp, (_, observed) in states:
        for index, leg in enumerate(LEGS):
            if not observed[index] and starts[leg] is None:
                starts[leg] = stamp
            elif observed[index] and starts[leg] is not None:
                episodes[leg].append((starts[leg], stamp))
                starts[leg] = None
    # An interval still open at stand is not a demonstrated recontact and is
    # kept explicitly as unbounded instead of inventing a landing transition.
    for leg in LEGS:
        if starts[leg] is not None:
            episodes[leg].append((starts[leg], None))
    return episodes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('bag', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument(
        '--allow-open-window', action='store_true',
        help='usar el final de la bolsa si falta stand/stop (solo exploración)')
    parser.add_argument(
        '--off-debounce', type=float, default=0.12,
        help='persistencia cruda exigida para declarar pérdida estable')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    start, stop, commands, mode = read_window(args.bag, args.allow_open_window)
    samples_per_cycle = 24 if mode == 'crawl' else 32
    states, phases = read_states(args.bag, start, stop, mode)
    if not states:
        raise RuntimeError('No hay diagnósticos válidos en la ventana')
    cycles = complete_cycles(phases, samples_per_cycle)
    filtered_states = states_with_component(states, 1)
    raw_states = states_with_component(states, 2)
    transition_rows, delay_summary = transition_analysis(filtered_states, start)
    write_csv(args.output / 'transiciones_contacto.csv', transition_rows)
    raw_delay_summary = None
    if raw_states:
        raw_rows, raw_delay_summary = transition_analysis(raw_states, start)
        write_csv(args.output / 'transiciones_contacto_crudo.csv', raw_rows)
        raw_episodes = contact_loss_episodes(raw_states, stop)
        episode_rows = []
        for leg in LEGS:
            for episode_start, episode_stop in raw_episodes[leg]:
                duration = ((episode_stop - episode_start) / 1e9
                            if episode_stop is not None else None)
                episode_rows.append({
                    'leg': leg,
                    'start_time_s': (episode_start - start) / 1e9,
                    'end_time_s': ((episode_stop - start) / 1e9
                                   if episode_stop is not None else ''),
                    'duration_s': duration if duration is not None else '',
                    'exceeds_off_debounce': (
                        duration >= args.off_debounce
                        if duration is not None else ''),
                    'bounded_by_recontact': episode_stop is not None,
                })
        with (args.output / 'episodios_sin_contacto_crudo.csv').open(
                'w', newline='', encoding='utf-8') as handle:
            writer = csv.DictWriter(handle, fieldnames=list(episode_rows[0]))
            writer.writeheader()
            writer.writerows(episode_rows)

    total, all_match, totals, matches = agreement(filtered_states, start, stop)
    raw_total = raw_all_match = 0.0
    raw_totals = raw_matches = None
    if raw_states:
        raw_total, raw_all_match, raw_totals, raw_matches = agreement(
            raw_states, start, stop)
    summary_rows = []
    for leg in LEGS:
        for transition in ('liftoff', 'landing'):
            values = delay_summary[(leg, transition)]
            summary_rows.append({
                'leg': leg,
                'transition': transition,
                'paired_transitions': len(values),
                'mean_delay_s': sum(values) / len(values) if values else '',
                'min_delay_s': min(values) if values else '',
                'max_delay_s': max(values) if values else '',
                'agreement_percent': 100.0 * matches[leg] / totals[leg]
                if totals[leg] else 0.0,
            })
    with (args.output / 'resumen_por_pata.csv').open(
            'w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary_rows[0]))
        writer.writeheader()
        writer.writerows(summary_rows)

    lines = [
        f'# Análisis de contactos medidos durante {"gateo" if mode == "crawl" else "marcha paso"}', '',
        f'- Bolsa: `{args.bag}`.',
        f'- Ventana {"gateo" if mode == "crawl" else "paso"}--stand: {(stop - start) / 1e9:.6f} s.',
        f'- Ciclos completos según `/nova/gait_phase`: {len(cycles)}.',
        f'- Índices de ciclo completos: {cycles}.',
        f'- Estados comprimidos analizados: {len(states)}.',
        f'- Coincidencia simultánea filtrada de las cuatro patas: '
        f'{100.0 * all_match / total:.3f} %.', '',
        '## Resultado por pata', '',
        '| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |',
        '|---|---:|---:|---:|',
    ]
    for leg in LEGS:
        lift = delay_summary[(leg, 'liftoff')]
        land = delay_summary[(leg, 'landing')]
        lift_text = f'{sum(lift) / len(lift):.6f} s' if lift else 'sin pares'
        land_text = f'{sum(land) / len(land):.6f} s' if land else 'sin pares'
        lines.append(
            f'| {leg} | {100.0 * matches[leg] / totals[leg]:.3f} % '
            f'| {lift_text} | {land_text} |')
    if raw_states:
        lines.extend(['', '## Comparación crudo frente a filtrado', '',
            f'- Coincidencia simultánea cruda: '
            f'{100.0 * raw_all_match / raw_total:.3f} %.',
            f'- Coincidencia simultánea filtrada: '
            f'{100.0 * all_match / total:.3f} %.', '',
            '| Pata | Coincidencia cruda | Coincidencia filtrada |',
            '|---|---:|---:|'])
        for leg in LEGS:
            lines.append(
                f'| {leg} | {100.0 * raw_matches[leg] / raw_totals[leg]:.3f} % '
                f'| {100.0 * matches[leg] / totals[leg]:.3f} % |')
        lines.extend(['',
            '| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |',
            '|---|---|---:|---:|'])
        for leg in LEGS:
            for transition in ('liftoff', 'landing'):
                raw_values = raw_delay_summary[(leg, transition)]
                filtered_values = delay_summary[(leg, transition)]
                raw_text = (f'{sum(raw_values) / len(raw_values):.6f} s'
                            if raw_values else 'sin pares')
                filtered_text = (
                    f'{sum(filtered_values) / len(filtered_values):.6f} s'
                    if filtered_values else 'sin pares')
                lines.append(
                    f'| {leg} | {transition} | {raw_text} | {filtered_text} |')
        lines.extend(['',
            f'Persistencia cruda exigida para declarar vuelo filtrado: '
            f'{args.off_debounce:.3f} s.', '',
            '| Pata | Episodios acotados | Duración media | Duración máxima '
            '| Episodios que superan el umbral |',
            '|---|---:|---:|---:|---:|'])
        for leg in LEGS:
            durations = [(end - begin) / 1e9 for begin, end in raw_episodes[leg]
                         if end is not None]
            exceeds = sum(value >= args.off_debounce for value in durations)
            mean_text = (f'{sum(durations) / len(durations):.6f} s'
                         if durations else 'sin episodios')
            max_text = (f'{max(durations):.6f} s'
                        if durations else 'sin episodios')
            lines.append(
                f'| {leg} | {len(durations)} | {mean_text} | {max_text} '
                f'| {exceeds} |')
    else:
        lines.extend(['',
            'Esta bolsa no contiene `raw_observed_contacts`; corresponde al '
            'formato histórico y solo permite analizar el estado observado.'])
    lines.extend(['',
        'Un retardo positivo indica que la transición medida ocurrió después '
        'de la prevista; uno negativo indica que ocurrió antes. Los pares se '
        'buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, '
        'no por número de mensajes.', '',
        'El análisis es descriptivo y no activa decisiones del supervisor.',
    ])
    (args.output / 'INFORME_CONTACTOS.md').write_text(
        '\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps({
        'duration_s': (stop - start) / 1e9,
        'complete_cycles': len(cycles),
        'all_feet_agreement_percent': 100.0 * all_match / total,
        'raw_all_feet_agreement_percent': (
            100.0 * raw_all_match / raw_total if raw_states else None),
        'output': str(args.output),
        'commands': commands,
    }, indent=2))


if __name__ == '__main__':
    main()
