#!/bin/bash
# https://stackoverflow.com/a/25735801/9876427
OPTIONS=""
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -a)
    ALGO="$2"
    shift
    ;;
    -e)
    EX_PATH="$2 $3"
    shift
    shift
    ;;
    -p|-t)
    OPTIONS="${OPTIONS}${1} "
    ;;
    *)
        echo "Argument inconnu: ${1}"
        exit
    ;;
esac
shift
done

python ./fetch.py
