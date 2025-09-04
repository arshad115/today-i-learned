#!/bin/bash

# Setup script to install the git pre-commit hook
# This will automatically update README.md when you commit changes to markdown files

set -e

echo "🔧 Setting up automatic README updates..."

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Error: This doesn't appear to be a git repository"
    exit 1
fi

# Create hooks directory if it doesn't exist
mkdir -p .git/hooks

# Copy the pre-commit hook
if [ -f "pre-commit-hook.sh" ]; then
    cp pre-commit-hook.sh .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    echo "✅ Git pre-commit hook installed successfully!"
    echo ""
    echo "🎯 What this does:"
    echo "   • Automatically runs README update script when you commit .md files"
    echo "   • Only triggers when markdown files in category folders are changed"
    echo "   • Automatically adds the updated README.md to your commit"
    echo ""
    echo "💡 Usage:"
    echo "   • Just commit normally: git commit -m 'Add new TIL'"
    echo "   • The README will be updated automatically if needed"
    echo "   • You can still run ./update_readme.sh manually anytime"
else
    echo "❌ Error: pre-commit-hook.sh not found"
    exit 1
fi

echo ""
echo "🚀 Setup complete! Your README will now update automatically when you commit TIL files."
