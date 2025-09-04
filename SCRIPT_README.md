# README Auto-Update Script

This directory contains scripts to automatically update the `README.md` file based on the markdown files in your TIL (Today I Learned) folders.

## Quick Start

### Option 1: Manual Updates (Simple)
```bash
./update_readme.sh
```

### Option 2: Automatic Updates (Recommended)
```bash
./setup_auto_update.sh
```
This installs a git hook that automatically updates README.md when you commit .md files.

## Files

- **`update_readme.py`** - Python script that scans folders and generates the README content
- **`update_readme.sh`** - Shell script wrapper for easier execution  
- **`setup_auto_update.sh`** - Installs git pre-commit hook for automatic updates
- **`pre-commit-hook.sh`** - Git hook that runs the update script automatically
- **`SCRIPT_README.md`** - This documentation file

## How It Works

The script automatically:

1. **Scans all folders** for `.md` files (ignoring empty folders)
2. **Extracts titles** from markdown files (prefers `# Header` or `## Header`, falls back to filename)
3. **Counts total TILs** and updates the count in the README
4. **Generates table of contents** with proper anchor links
5. **Creates category sections** with sorted file lists
6. **Preserves header and footer** content from the existing README

## Usage Options

### Manual Updates
Run whenever you want to update the README:
```bash
./update_readme.sh
```

### Automatic Updates with Git Hooks
Set up once, then forget about it:
```bash
./setup_auto_update.sh
```

After setup, the README will automatically update when you:
```bash
git add new-til-file.md
git commit -m "Add new TIL"  # README updates automatically!
```

### Direct Python Script
```bash
python3 update_readme.py
```

## When to Run

Run this script whenever you:
- Add new `.md` files to any category folder
- Create new category folders with TIL files
- Want to ensure the README is up-to-date with accurate counts and links

## Features

### Automatic Title Extraction
The script intelligently extracts titles from markdown files:
1. First tries to find `# Title` (H1 header)
2. Falls back to `## Title` (H2 header)
3. If no headers found, converts filename to title case

### Category Mapping
Special category names are automatically converted:
- `angular2` → `Angular 2+`
- `csharp` → `C#`
- `javascript` → `JavaScript`
- `nodejs` → `Node.js`
- `vuejs` → `Vue.js`

### Smart Sorting
- Categories are sorted alphabetically by display name
- Files within categories are sorted alphabetically by title
- Anchor links are generated automatically for table of contents

### Git Integration
- Pre-commit hook only runs when .md files in category folders change
- Automatically stages the updated README.md
- Preserves your commit workflow

## Example Output

```
✅ README.md updated successfully!
📊 Total TILs: 126
📁 Categories: 20

📋 Categories found:
  • Android: 5 files
  • Angular 2+: 18 files
  • Python: 37 files
  ...
```

## Requirements

- Python 3.6+
- Git (for automatic updates)
- No external dependencies (uses only standard library)

## Troubleshooting

If the script doesn't work as expected:

1. **Check file permissions**: Make sure the script can read your `.md` files
2. **Verify Python version**: Run `python3 --version` to ensure you have Python 3.6+
3. **Check directory structure**: The script should be run from the TIL repository root directory
4. **Git hook issues**: If automatic updates don't work, check `.git/hooks/pre-commit` exists and is executable

## Customization

You can customize the script by modifying:

- **Category mappings** in the `get_category_display_name()` function
- **Title extraction logic** in the `extract_title_from_markdown()` function  
- **Footer content** in the `update_readme()` function

## Safety

The script preserves:
- Front matter (Jekyll configuration at the top)
- Header content (description, badges, etc.)
- Footer content (cat gif, inspiration, license, etc.)

Only the categories table of contents and category sections are regenerated.

## Workflow Examples

### Adding a New TIL (with automatic updates)
```bash
# 1. Create your new TIL file
echo "# How to do something cool" > javascript/cool-feature.md

# 2. Add and commit (README updates automatically!)
git add javascript/cool-feature.md
git commit -m "Add TIL about cool JavaScript feature"
```

### Adding a New Category
```bash
# 1. Create new folder and TIL
mkdir machine-learning
echo "# Introduction to ML" > machine-learning/intro-to-ml.md

# 2. Commit (README automatically adds new category!)
git add machine-learning/
git commit -m "Add machine learning category"
```

### Manual Update
```bash
# Run anytime to sync README with current files
./update_readme.sh
```
