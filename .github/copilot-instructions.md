# GitHub Copilot Instructions for Today I Learned Project

## Project Overview
This is a "Today I Learned" (TIL) repository of short markdown notes. The notes are also published on arshadmehmood.com. README listings come from `update_readme.py`. This is not a Jekyll site.

## File Structure
- Each TIL is a markdown file in a category-specific subfolder
- Categories: android, angular2, csharp, css, docker, firebase, git, github, javascript, jekyll, kubernetes, nginx, nodejs, php, python, sql, typescript, vuejs, etc.
- Files should follow the naming convention: `kebab-case-description.md`

## Content Guidelines
1. **File Naming**: Use descriptive, kebab-case filenames (e.g., `build-and-push-with-docker.md`)
2. **Front matter**: Start every note with YAML `title:`. Optional `date:` and `excerpt:` are allowed.
3. **No duplicate H1**: The blog layout prints the title. Do not repeat it as `# Title` in the body.
4. **No Liquid**: Do not wrap Angular `{{ }}` examples in `{% raw %}`. Plain markdown is enough.
5. **Categories**: Place files in appropriate category folders. Create new folders if needed.

## Purpose
- When I add a new TIL file or a few lines of code, expand it into a small, self-contained entry that teaches the concept: brief explanation of how/why, 1–2 alternatives, optional extra code if it helps, and practical tips.

## When to act
- I create or edit a markdown file in the TIL repo (any category folder).
- The file may contain only a title, a short note, or a small code snippet.

## Automated Systems
- The `update_readme.py` script reads YAML `title:` and updates the main README.md
- The `setup_auto_update.sh` sets up automatic README updates

## When Adding New TILs
1. Create the markdown file in the appropriate category folder
2. Use a YAML `title:` and a clear, descriptive slug
3. Include practical code examples when relevant
4. Keep content concise but complete
5. Run `python3 update_readme.py` to refresh README if needed

## When Editing Existing Content
- Keep YAML `title:` in sync with the note
- Preserve the automated numbering and categorization
- Update content while keeping the learning-focused approach

## Development Notes
- This is part of a larger blog ecosystem (arshadmehmood.com)
- The TIL content is also published on the main blog
- Maintain consistency with the overall blog's tone and style

## Don’ts
- Don’t introduce frameworks/tooling unrelated to the snippet.
- Don’t over-engineer or turn this into a full tutorial.
- Don’t add Jekyll/Minimal Mistakes fields, `{% raw %}`, or a body H1 that duplicates `title:`.
