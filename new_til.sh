#!/bin/bash
# TIL Generator - Shell Wrapper
# Makes it easy to create new TIL entries

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to the script directory
cd "$SCRIPT_DIR"

# Run the Python script
python3 new_til.py
