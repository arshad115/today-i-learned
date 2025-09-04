#!/usr/bin/env python3
"""
Script to automatically update the README.md file for the Today I Learned repository.
This script scans all folders for markdown files and generates:
1. Total count of TILs
2. Categories table of contents
3. Content sections for each category with proper links and titles
"""

import os
import re
from pathlib import Path


def extract_title_from_markdown(file_path):
    """Extract the title from a markdown file, preferring H1 headers, then filename."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Look for H1 header (# Title)
        h1_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if h1_match:
            return h1_match.group(1).strip()
        
        # Look for H2 header (## Title) as fallback
        h2_match = re.search(r'^## (.+)$', content, re.MULTILINE)
        if h2_match:
            return h2_match.group(1).strip()
            
        # If no headers found, use filename and convert to title case
        filename = Path(file_path).stem
        # Convert kebab-case or snake_case to title case
        title = filename.replace('-', ' ').replace('_', ' ')
        title = ' '.join(word.capitalize() for word in title.split())
        return title
        
    except Exception as e:
        # Fallback to filename if there's any error reading the file
        filename = Path(file_path).stem
        title = filename.replace('-', ' ').replace('_', ' ')
        title = ' '.join(word.capitalize() for word in title.split())
        return title


def get_category_display_name(folder_name):
    """Convert folder name to a display-friendly category name with emojis."""
    category_mappings = {
        'android': '🤖 Android',
        'angular2': '🅰️ Angular 2+',
        'csharp': '💎 C#',
        'css': '🎨 CSS',
        'docker': '🐳 Docker',
        'facebook': '📘 Facebook',
        'firebase': '🔥 Firebase',
        'git': '📝 Git',
        'github': '🐙 GitHub',
        'javascript': '⚡ JavaScript',
        'jekyll': '💎 Jekyll',
        'kubernetes': '☸️ Kubernetes',
        'nginx': '🌐 Nginx',
        'nodejs': '💚 Node.js',
        'other': '🔧 Other',
        'php': '🐘 PHP',
        'programming': '💻 Programming',
        'python': '🐍 Python',
        'sql': '🗄️ SQL',
        'typescript': '📘 TypeScript',
        'vuejs': '💚 Vue.js'
    }
    
    if folder_name in category_mappings:
        return category_mappings[folder_name]
    
    # Default: capitalize first letter with generic emoji
    return f'📚 {folder_name.capitalize()}'


def generate_anchor_link(category_name):
    """Generate anchor link for table of contents."""
    # Remove emoji and convert to lowercase and replace spaces/special chars with hyphens
    # First remove emojis and extra spaces
    clean_name = re.sub(r'[^\w\s-]', '', category_name).strip()
    anchor = clean_name.lower()
    anchor = re.sub(r'\s+', '-', anchor)  # Replace spaces with hyphens
    anchor = re.sub(r'-+', '-', anchor)  # Replace multiple hyphens with single
    return anchor.strip('-')


def scan_til_folders():
    """Scan all folders and collect TIL information."""
    script_dir = Path(__file__).parent
    categories = {}
    total_count = 0
    
    # Get all directories (excluding hidden ones and specific files)
    exclude_items = {'.git', '.gitignore', 'LICENSE', 'README.md', '_config.yml', '.DS_Store'}
    
    for item in script_dir.iterdir():
        if item.is_dir() and item.name not in exclude_items:
            folder_name = item.name
            md_files = []
            
            # Find all markdown files in this directory
            for md_file in item.glob('*.md'):
                title = extract_title_from_markdown(md_file)
                relative_path = f"{folder_name}/{md_file.name}"
                md_files.append({
                    'title': title,
                    'path': relative_path,
                    'filename': md_file.name
                })
                total_count += 1
            
            # Only include categories that have markdown files
            if md_files:
                # Sort files alphabetically by title
                md_files.sort(key=lambda x: x['title'].lower())
                
                categories[folder_name] = {
                    'display_name': get_category_display_name(folder_name),
                    'files': md_files
                }
    
    return categories, total_count


def generate_usage_section():
    """Generate a usage/navigation section."""
    usage_lines = ["### 🚀 How to Use This Repository", ""]
    
    usage_lines.extend([
        "📖 **Browse by Category**: Click on any category below to jump to that section",
        "🔍 **Search**: Use `Ctrl+F` (or `Cmd+F` on Mac) to search for specific topics",
        "🌐 **Web Version**: Visit [arshadmehmood.com/today-i-learned](https://arshadmehmood.com/today-i-learned/) for a better reading experience",
        "⭐ **Star this repo**: If you find it useful, consider giving it a star!",
        "",
    ])
    
    return usage_lines


def generate_stats_section(categories, total_count):
    """Generate a quick stats section."""
    stats_lines = ["### 📊 Quick Stats", ""]
    
    # Sort categories by file count (descending)
    sorted_by_count = sorted(categories.items(), key=lambda x: len(x[1]['files']), reverse=True)
    
    stats_lines.append(f"🎯 **Total TILs:** {total_count}")
    stats_lines.append(f"📁 **Categories:** {len(categories)}")
    stats_lines.append("")
    stats_lines.append("🔥 **Top Categories:**")
    
    # Show top 5 categories
    for i, (folder_name, category_info) in enumerate(sorted_by_count[:5], 1):
        display_name = category_info['display_name']
        count = len(category_info['files'])
        stats_lines.append(f"{i}. {display_name}: **{count}** TILs")
    
    stats_lines.append("")
    return stats_lines


def generate_table_of_contents(categories):
    """Generate the table of contents section."""
    toc_lines = ["### 📋 Categories", ""]
    
    # Sort categories alphabetically by the actual category name (without emoji)
    sorted_categories = sorted(categories.items(), key=lambda x: x[1]['display_name'].split(' ', 1)[-1].lower())
    
    for folder_name, category_info in sorted_categories:
        display_name = category_info['display_name']
        anchor = generate_anchor_link(display_name)
        toc_lines.append(f"* [{display_name}](#{anchor})")
    
    return toc_lines


def generate_category_sections(categories):
    """Generate the content sections for each category."""
    sections = []
    
    # Sort categories alphabetically by the actual category name (without emoji)
    sorted_categories = sorted(categories.items(), key=lambda x: x[1]['display_name'].split(' ', 1)[-1].lower())
    
    for folder_name, category_info in sorted_categories:
        display_name = category_info['display_name']
        files = category_info['files']
        
        sections.append(f"### {display_name}")
        
        for file_info in files:
            title = file_info['title']
            path = file_info['path']
            sections.append(f"- [{title}]({path})")
        
        sections.append("")  # Empty line after each section
    
    return sections


def update_readme():
    """Update the README.md file with the latest TIL information."""
    script_dir = Path(__file__).parent
    readme_path = script_dir / "README.md"
    
    # Scan for TILs
    categories, total_count = scan_til_folders()
    
    if total_count == 0:
        print("No TIL files found!")
        return
    
    # Generate new content
    usage_lines = generate_usage_section()
    stats_lines = generate_stats_section(categories, total_count)
    toc_lines = generate_table_of_contents(categories)
    category_sections = generate_category_sections(categories)
    
    # Read existing README to preserve header and footer
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract the header part (everything before "### Categories" or "### 📋 Categories")
    header_match = re.search(r'^(.*?)^### (?:📋 )?Categories', content, re.MULTILINE | re.DOTALL)
    if not header_match:
        print("Could not find the Categories section in README.md")
        return

    header = header_match.group(1).rstrip()
    
    # Clean up any extra --- separators at the end of header
    header_lines = header.split('\n')
    while header_lines and header_lines[-1].strip() == '---':
        header_lines.pop()
    header = '\n'.join(header_lines)    # Update the TIL count in the header with emoji
    header = re.sub(r'_\d+ TILs and counting\.\.\._', f'_📚 {total_count} TILs and counting... 🚀_', header)
    
    # Extract the footer part (everything from "---" before "### Catz" or "### 🐱 Catz")
    footer_match = re.search(r'^---\s*^### (?:🐱 )?Catz.*$', content, re.MULTILINE | re.DOTALL)
    if footer_match:
        footer = footer_match.group(0)
    else:
        # Default footer if not found
        footer = """---
### 🐱 Catz
![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)

## 💡 Inspiration
I shamelessly stole this idea from [wajahatkarim3/Today-I-Learned](https://github.com/wajahatkarim3/Today-I-Learned), then I also saw other similar repositories and decided to share my own repo of what I learn everyday.

## 🤝 Contributing

The best way you can contribute is to support the idea of keeping track of things you learned. Just create a public repo and start writing and sharing notes. This is way better than keeping them to yourself.

## 📄 License

&copy; 2018-2025 Arshad Mehmood

This repository is licensed under the MIT license. See `LICENSE` for
details."""
    
    # Combine all parts
    new_content_parts = [
        header,
        "",
        "---",
        "",
        "\n".join(usage_lines),
        "\n".join(stats_lines),
        "\n".join(toc_lines),
        "",
        "---",
        "",
        "\n".join(category_sections).rstrip(),
        footer
    ]
    
    new_content = "\n".join(new_content_parts)
    
    # Write the updated README
    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f"✅ README.md updated successfully!")
    print(f"📊 Total TILs: {total_count}")
    print(f"📁 Categories: {len(categories)}")
    
    # Show categories with counts
    print("\n📋 Categories found:")
    sorted_categories = sorted(categories.items(), key=lambda x: x[1]['display_name'].lower())
    for folder_name, category_info in sorted_categories:
        display_name = category_info['display_name']
        count = len(category_info['files'])
        print(f"  • {display_name}: {count} file{'s' if count != 1 else ''}")


if __name__ == "__main__":
    update_readme()
