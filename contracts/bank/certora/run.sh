#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <.sol file> <contract name> <.spec file>"
    exit 1
fi


echo "Executing: certoraRun $1:$2 --verify $2:$3"

certoraRun $1:$2 --verify $2:$3
