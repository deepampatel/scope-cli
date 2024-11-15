#!/bin/bash

# Stop on errors
set -e

echo "Cleaning previous builds..."
rm -rf dist/

echo "Building package..."
python setup.py sdist bdist_wheel

echo "Build complete. Files in ./dist/"
ls -l dist/
