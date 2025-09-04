# GitHub Copilot Instructions for Today I Learned Project

## Project Overview
This is a "Today I Learned" (TIL) repository that documents small snippets of code and learning experiences. It's structured as a Jekyll blog with automatic README generation.

## File Structure
- Each TIL is a markdown file in a category-specific subfolder
- Categories: android, angular2, csharp, css, docker, firebase, git, github, javascript, jekyll, kubernetes, nginx, nodejs, php, python, sql, typescript, vuejs, etc.
- Files should follow the naming convention: `kebab-case-description.md`

## Content Guidelines
1. **File Naming**: Use descriptive, kebab-case filenames (e.g., `build-and-push-with-docker.md`)
2. **Content Structure**: Each TIL should be concise and focused on one specific learning
3. **Categories**: Place files in appropriate category folders. Create new folders if needed.
4. **Markdown Format**: Use standard markdown with code blocks for examples

## Purpose
- When I add a new TIL file or a few lines of code, expand it into a small, self-contained entry that teaches the concept: brief explanation of how/why, 1–2 alternatives, optional extra code if it helps, and practical tips. Do not add front matter. Keep everything plain Markdown.

## When to act
- I create or edit a markdown file in the TIL repo (any category folder).
- The file may contain only a title, a short note, or a small code snippet.

## Automated Systems
- The `update_readme.py` script automatically updates the main README.md with TIL counts and listings
- The `setup_auto_update.sh` sets up automatic README updates
- Jekyll configuration in `_config.yml` handles blog generation

## When Adding New TILs
1. Create the markdown file in the appropriate category folder
2. Use clear, descriptive titles
3. Include practical code examples when relevant
4. Keep content concise but complete
5. Run the update script to refresh README if needed

## When Editing Existing Content
- Maintain the existing structure and format
- Preserve the automated numbering and categorization
- Update content while keeping the learning-focused approach

## Development Notes
- This is part of a larger blog ecosystem (arshadmehmood.com)
- The TIL content is also published on the main blog
- Maintain consistency with the overall blog's tone and style

## Don’ts
- Don’t introduce frameworks/tooling unrelated to the snippet.
- Don’t over-engineer or turn this into a full tutorial.
- Don’t assume front matter or blog generators.