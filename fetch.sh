#!/bin/bash
python -m venv .
pip install -r requirements.txt

python ./fetch.py
