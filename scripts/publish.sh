#!/bin/bash

# Stop on errors
set -e

# Ensure the build exists
if [ ! -d "dist" ]; then
    echo "Build directory does not exist. Run scripts/build.sh first."
    exit 1
fi

echo "Publishing to PyPI..."
twine upload dist/*

echo "Publish complete!"
