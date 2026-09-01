#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build Thesis.tex
cp build/Thesis.pdf Documento_TESIS_PRELIMINAR.pdf
printf 'PDF generado: %s\n' "$(pwd)/Documento_TESIS_PRELIMINAR.pdf"
