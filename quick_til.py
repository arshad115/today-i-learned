#!/usr/bin/env python3
"""
Quick TIL Generator
Creates a new TIL entry with minimal prompts - perfect for quick learning notes.
Usage: python3 quick_til.py "TIL Title" category [content]
"""

import os
import sys
from datetime import datetime
import re

def slugify(text):
    """Convert text to URL-friendly slug"""
    slug = text.lower().strip()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s-]+', '-', slug)
    slug = slug.strip('-')
    return slug

def create_quick_til(title, category, content=""):
    """Create a TIL entry with minimal setup"""
    
    # Generate filename
    slug = slugify(title)
    filename = f"{slug}.md"
    
    # Create category directory if it doesn't exist
    category_dir = category
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)
        print(f"📁 Created new category: {category_dir}")
    
    filepath = os.path.join(category_dir, filename)
    
    # Check if file already exists
    if os.path.exists(filepath):
        print(f"❌ File {filename} already exists in {category}!")
        return False
    
    # Create TIL content
    til_content = f"# {title}\n\n"
    
    if content:
        til_content += f"{content}\n"
    else:
        til_content += "<!-- Add your TIL content here -->\n\n"
    
    # Write the file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(til_content)
        
        print(f"✅ Created TIL: {filepath}")
        return True
        
    except Exception as e:
        print(f"❌ Error creating file: {e}")
        return False

def show_usage():
    """Show usage information"""
    print("🎓 Quick TIL Generator")
    print("=" * 30)
    print("Usage:")
    print('  python3 quick_til.py "TIL Title" category [content]')
    print()
    print("Examples:")
    print('  python3 quick_til.py "Docker Multi-stage Builds" docker')
    print('  python3 quick_til.py "Git Rebase vs Merge" git "Key differences between rebase and merge"')
    print()
    print("Available categories:")
    categories = []
    for item in os.listdir('.'):
        if os.path.isdir(item) and not item.startswith('.') and not item.startswith('_'):
            if any(f.endswith('.md') for f in os.listdir(item) if os.path.isfile(os.path.join(item, f))):
                categories.append(item)
    
    if categories:
        print(f"  {', '.join(sorted(categories))}")
    else:
        print("  No existing categories found")
    print("\n💡 You can create new categories by using a new category name")

def main():
    """Main function"""
    if len(sys.argv) < 3:
        show_usage()
        sys.exit(1)
    
    title = sys.argv[1]
    category = sys.argv[2]
    content = sys.argv[3] if len(sys.argv) > 3 else ""
    
    if not title or not category:
        print("❌ Title and category are required!")
        show_usage()
        sys.exit(1)
    
    print(f"🚀 Creating quick TIL: {title}")
    success = create_quick_til(title, category, content)
    
    if success:
        print(f"🎉 TIL created successfully!")
        print(f"💡 Update README: python3 update_readme.py")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
