#!/usr/bin/env python3
"""Audita que las observaciones físicas usadas por PPO existan en cada rosbag."""
import argparse, math, json
from pathlib import Path
from rosbag2_py import SequentialReader, StorageOptions, ConverterOptions
from rosidl_runtime_py.utilities import get_message
from rclpy.serialization import deserialize_message

TOPICS=['/nova/imu','/world/empty/dynamic_pose/info','/nova/contact_diagnostics','/joint_states']
def audit(path):
    r=SequentialReader(); r.open(StorageOptions(uri=str(path),storage_id='sqlite3'),ConverterOptions('cdr','cdr'))
    types={x.name:x.type for x in r.get_all_topics_and_types()}; out={t:0 for t in TOPICS}; finite_imu=0; heights=[]; contacts=[]
    while r.has_next():
        topic,raw,_=r.read_next()
        if topic not in TOPICS: continue
        out[topic]+=1; m=deserialize_message(raw,get_message(types[topic]))
        if topic=='/nova/imu':
            vals=[m.linear_acceleration.x,m.linear_acceleration.y,m.linear_acceleration.z,m.angular_velocity.x,m.angular_velocity.y,m.angular_velocity.z]
            finite_imu += int(all(math.isfinite(float(v)) for v in vals))
        elif topic=='/world/empty/dynamic_pose/info':
            for tr in m.transforms:
                if tr.child_frame_id in ('nova_sm3','base_link') or not tr.child_frame_id: heights.append(tr.transform.translation.z); break
        elif topic=='/nova/contact_diagnostics':
            contacts.append(m.data)
    out['imu_muestras_finitas']=finite_imu; out['altura_muestras']=len(heights); out['altura_min_m']=min(heights) if heights else None; out['altura_max_m']=max(heights) if heights else None; out['contactos_no_vacios']=sum(bool(x) for x in contacts); return out
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('root',type=Path); args=ap.parse_args(); results={}
    bags=list(args.root.glob('ppo_gazebo_*/bag_0.db3'))+list(args.root.glob('semilla_*/bag_0.db3'))
    for bag in sorted(bags): results[bag.parent.name]=audit(bag.parent)
    print(json.dumps(results,indent=2,ensure_ascii=False)); (args.root/'auditoria_observaciones.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
if __name__=='__main__': main()
