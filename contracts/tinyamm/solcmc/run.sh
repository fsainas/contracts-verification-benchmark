#!/bin/bash

if [ $# -eq 0 ] 
then
  echo "Please provide a .sol file."
  exit 1
fi

timeout=${2:-0}

echo "Executing: time solc $1 --model-checker-engine chc --model-checker-timeout $timeout --model-checker-targets \"assert\" --model-checker-show-unproved"

time solc $1 --model-checker-engine chc --model-checker-timeout $timeout --model-checker-targets "assert" --model-checker-show-unproved
