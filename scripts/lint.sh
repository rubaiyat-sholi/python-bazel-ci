#!/bin/bash
set -e

# Install pylint if not installed
pip install pylint

# Run pylint on all Python files
pylint src/*.py tests/*.py --fail-under=8.0
