#!/bin/bash

# Git pre-commit hook to automatically update README.md
# This script runs before each commit to ensure the README is up-to-date
# 
# To install this hook:
# 1. Copy this file to .git/hooks/pre-commit
# 2. Make it executable: chmod +x .git/hooks/pre-commit

set -e

# Check if we're in the TIL directory
if [ ! -f "update_readme.py" ]; then
    echo "⚠️  Warning: update_readme.py not found. Skipping README update."
    exit 0
fi

# Check if any .md files in category folders have been added/modified
if git diff --cached --name-only | grep -E '^[^/]+/.*\.md$' > /dev/null; then
    echo "📝 Markdown files detected in category folders. Updating README..."
    
    # Run the update script
    python3 update_readme.py
    
    # Add the updated README to the commit if it was changed
    if git diff --name-only | grep "README.md" > /dev/null; then
        echo "📄 Adding updated README.md to commit"
        git add README.md
    fi
    
    echo "✅ README.md updated and staged for commit"
else
    echo "ℹ️  No category markdown files changed. Skipping README update."
fi

exit 0
