#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
mkdir -p "$script_dir/build"
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir="$script_dir/build" "$script_dir/main.tex"
cp "$script_dir/build/main.pdf" "$script_dir/main.pdf"
