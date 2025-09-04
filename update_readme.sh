#!/bin/bash

# Script to update the Today I Learned README.md file
# This script automatically scans all folders for markdown files and updates the README

set -e

echo "🔄 Updating Today I Learned README..."
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to the script directory
cd "$SCRIPT_DIR"

# Run the Python script
python3 update_readme.py

echo ""
echo "✨ All done! Your README.md has been updated with the latest TILs."
echo ""
echo "💡 Usage tips:"
echo "   • Run this script whenever you add new .md files to any category folder"
echo "   • The script will automatically count all TILs and update links"
echo "   • To add a new category, just create a new folder with .md files"
echo "   • Empty folders are ignored"
