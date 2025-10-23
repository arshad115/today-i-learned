# TIL Creation Scripts

This directory contains scripts to easily create new TIL (Today I Learned) entries, similar to the blog post creation scripts.

## Available Scripts

### 1. Interactive TIL Creator (`new_til.py`)
Full interactive TIL creation with templates and prompts.

**Usage:**
```bash
python3 new_til.py
# or
./new_til.sh
```

**Features:**
- Interactive prompts for title and category
- Shows available categories
- Allows creating new categories
- Optional initial content input
- Creates structured TIL with template sections
- Option to open file after creation

### 2. Quick TIL Creator (`quick_til.py`)
Command-line TIL creation for quick entries.

**Usage:**
```bash
python3 quick_til.py "TIL Title" category [content]
```

**Examples:**
```bash
python3 quick_til.py "Docker Multi-stage Builds" docker
python3 quick_til.py "Git Rebase vs Merge" git "Key differences explained"
```

**Features:**
- Command-line interface for speed
- Automatic category creation
- Optional content parameter
- Minimal template

### 3. Setup Aliases (`setup_til_aliases.sh`)
Sets up convenient shell aliases for TIL creation.

**Usage:**
```bash
./setup_til_aliases.sh
```

**Creates these aliases:**
- `new-til` - Interactive TIL creator
- `quick-til` - Command-line TIL creator  
- `update-til` - Update README with all TILs
- `til-dir` - Navigate to TIL directory

## Quick Start

1. **Set up aliases (one-time setup):**
   ```bash
   ./setup_til_aliases.sh
   source ~/.zshrc  # or restart terminal
   ```

2. **Create a new TIL (interactive):**
   ```bash
   new-til
   ```

3. **Create a quick TIL:**
   ```bash
   quick-til "My New Learning" javascript "Learned about async/await"
   ```

4. **Update the README:**
   ```bash
   update-til
   ```

## TIL Structure

The scripts create TIL files with this structure:

```markdown
# Title

<!-- Content here -->

## Summary

## Details

## Example

```
# Code example
```

## References

- [Link](https://example.com)
```

## Available Categories

The scripts automatically detect existing categories from the directory structure:
- android
- angular2
- csharp
- css
- docker
- facebook
- firebase
- git
- github
- javascript
- jekyll
- kubernetes
- nginx
- nodejs
- other
- php
- programming
- python
- sql
- typescript
- vuejs

You can also create new categories by simply typing a new category name when prompted.

## Integration with Existing Workflow

These scripts work seamlessly with your existing TIL workflow:
- Use `update_readme.py` to update the main README after creating TILs
- The auto-update system will pick up new TILs automatically
- File naming follows the existing convention (kebab-case)

## Comparison with Blog Scripts

| Feature | Blog Scripts | TIL Scripts |
|---------|-------------|-------------|
| Front matter | Jekyll YAML | Simple markdown |
| Templates | Full blog template | Minimal TIL structure |
| Categories | Blog categories | Directory-based |
| Dating | Date-prefixed files | Simple filenames |
| Target | Published blog posts | Learning notes |
