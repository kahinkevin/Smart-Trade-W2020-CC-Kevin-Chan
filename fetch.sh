#!/bin/bash
# https://stackoverflow.com/a/42907421/9876427 for installing pip et virtualenv
# https://stackoverflow.com/a/25735801/9876427

#python -m venv .
virtualenv -q -p . $1
source $1/bin/activate
pip install -r requirements.txt

python ./fetch.py
