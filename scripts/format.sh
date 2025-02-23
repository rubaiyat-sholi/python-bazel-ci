#!/bin/bash
set -e

# Install black if not installed
pip install black

# Run black to check formatting
black --check src/ tests/
