#!/bin/bash

if [ $# -eq 0 ] 
then
  echo "Please provide a .sol file."
  exit 1
fi

echo "Executing: time solc $1 --model-checker-engine chc --model-checker-timeout 0 --model-checker-targets \"assert\" "

time solc $1 --model-checker-engine chc --model-checker-timeout 0 --model-checker-targets "assert"
