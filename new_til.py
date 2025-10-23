#!/usr/bin/env python3
"""
TIL (Today I Learned) Generator
Creates a new TIL entry with proper structure and filename.
"""

import os
import sys
from datetime import datetime
import re

def slugify(text):
    """Convert text to URL-friendly slug"""
    # Convert to lowercase and replace spaces with hyphens
    slug = text.lower().strip()
    # Remove special characters except hyphens and alphanumeric
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    # Replace spaces and multiple hyphens with single hyphen
    slug = re.sub(r'[\s-]+', '-', slug)
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    return slug

def get_categories():
    """Get available categories from existing TIL directories"""
    categories = []
    
    # Get all directories that contain .md files
    for item in os.listdir('.'):
        if os.path.isdir(item) and not item.startswith('.') and not item.startswith('_'):
            # Check if directory contains markdown files
            if any(f.endswith('.md') for f in os.listdir(item) if os.path.isfile(os.path.join(item, f))):
                categories.append(item)
    
    return sorted(categories)

def create_til_entry(title, category, content=""):
    """Create a new TIL entry"""
    
    # Generate filename
    slug = slugify(title)
    filename = f"{slug}.md"
    
    # Create category directory if it doesn't exist
    category_dir = category
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)
        print(f"📁 Created new category directory: {category_dir}")
    
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
        til_content += "<!-- Write your TIL content here -->\n\n"
        til_content += "## Summary\n\n"
        til_content += "## Details\n\n"
        til_content += "## Example\n\n"
        til_content += "```\n"
        til_content += "# Add your code example here\n"
        til_content += "```\n\n"
        til_content += "## References\n\n"
        til_content += "- [Link](https://example.com)\n"
    
    # Write the file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(til_content)
        
        print(f"✅ Created TIL: {filepath}")
        print(f"📝 Title: {title}")
        print(f"📂 Category: {category}")
        print(f"🔗 Path: {filepath}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating file: {e}")
        return False

def main():
    """Main function to create a new TIL entry"""
    print("🎓 TIL (Today I Learned) Generator")
    print("=" * 40)
    
    # Get title
    title = input("📝 Enter TIL title: ").strip()
    if not title:
        print("❌ Title is required!")
        sys.exit(1)
    
    # Get available categories
    existing_categories = get_categories()
    
    print(f"\n📂 Available categories: {', '.join(existing_categories)}")
    print("💡 You can also create a new category by typing a new name")
    
    category = input("📂 Enter category: ").strip()
    if not category:
        print("❌ Category is required!")
        sys.exit(1)
    
    # Ask if user wants to add initial content
    add_content = input("\n📄 Add initial content? (y/N): ").strip().lower()
    content = ""
    
    if add_content in ['y', 'yes']:
        print("📝 Enter your TIL content (press Ctrl+D when done):")
        print("💡 You can use markdown formatting")
        print("-" * 30)
        
        try:
            lines = []
            while True:
                try:
                    line = input()
                    lines.append(line)
                except EOFError:
                    break
            content = '\n'.join(lines)
        except KeyboardInterrupt:
            print("\n\n❌ Cancelled by user")
            sys.exit(1)
    
    # Create the TIL entry
    print(f"\n🚀 Creating TIL entry...")
    success = create_til_entry(title, category, content)
    
    if success:
        print(f"\n🎉 TIL entry created successfully!")
        print(f"💡 Don't forget to update the README by running: python3 update_readme.py")
        
        # Ask if user wants to open the file
        try:
            open_file = input("\n📖 Open the file now? (y/N): ").strip().lower()
            if open_file in ['y', 'yes']:
                filepath = os.path.join(category, f"{slugify(title)}.md")
                os.system(f"open '{filepath}'")
        except KeyboardInterrupt:
            pass
    else:
        print("❌ Failed to create TIL entry")
        sys.exit(1)

if __name__ == "__main__":
    main()
