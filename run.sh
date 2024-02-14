#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 foldername"
    exit 1
fi

FOLDER="$1"
PY_FILE=$(find "$FOLDER" -name '*.py')

# get just filename from the full path
PY_FILE=$(basename "$PY_FILE")

if [ -z "$PY_FILE" ]; then
    echo "No Python file found in the specified folder."
    exit 1
fi

docker run -it --rm --name python-running-script -v "$PWD/$FOLDER":/usr/src/myapp -w /usr/src/myapp python:3 python "$PY_FILE"
