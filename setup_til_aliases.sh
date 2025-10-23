#!/bin/bash
# Setup aliases for TIL generation
# Run this once to add aliases to your shell profile

# Get the directory where this script is located (should be the TIL root)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TIL_DIR="$SCRIPT_DIR"

# Verify this looks like a TIL directory
if [[ ! -f "$TIL_DIR/README.md" ]] || [[ ! -f "$TIL_DIR/update_readme.py" ]]; then
    echo "❌ This doesn't appear to be a TIL directory"
    echo "   Missing README.md or update_readme.py"
    echo "   Current directory: $TIL_DIR"
    exit 1
fi

SHELL_PROFILE=""

# Detect shell profile
if [ -f ~/.zshrc ]; then
    SHELL_PROFILE="$HOME/.zshrc"
elif [ -f ~/.bashrc ]; then
    SHELL_PROFILE="$HOME/.bashrc"
elif [ -f ~/.bash_profile ]; then
    SHELL_PROFILE="$HOME/.bash_profile"
else
    echo "❌ Could not find shell profile file"
    exit 1
fi

echo "🔧 Setting up TIL generation aliases..."
echo "📁 Using TIL directory: $TIL_DIR"
echo "📝 Adding to: $SHELL_PROFILE"

# Create backup
cp "$SHELL_PROFILE" "${SHELL_PROFILE}.backup"

# Add aliases
cat >> "$SHELL_PROFILE" << EOF

# TIL (Today I Learned) Generation Aliases
alias new-til='cd "$TIL_DIR" && python3 new_til.py'
alias quick-til='cd "$TIL_DIR" && python3 quick_til.py'
alias update-til='cd "$TIL_DIR" && python3 update_readme.py'
alias til-dir='cd "$TIL_DIR"'
EOF

echo ""
echo "✅ Aliases added successfully!"
echo ""
echo "📋 Available commands after restarting your terminal:"
echo "   • new-til       - Interactive TIL creator"
echo "   • quick-til     - Command-line TIL creator"
echo "   • update-til    - Update README with all TILs"
echo "   • til-dir       - Navigate to TIL directory"
echo ""
echo "📖 Usage examples:"
echo '   new-til'
echo '   quick-til "Docker Multi-stage Builds" docker'
echo '   quick-til "Git Rebase vs Merge" git "Key differences explained"'
echo '   update-til'
echo ""
echo "🔄 Restart your terminal or run: source $SHELL_PROFILE"
