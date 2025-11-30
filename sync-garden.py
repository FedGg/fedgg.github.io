#!/usr/bin/env python3
import os
import re
import shutil
from pathlib import Path
import yaml

# Configuration
SOURCE_VAULT = "/Users/federico/Obsidian/FG/AllNotes"
DEST_NOTES = "/Users/federico/Documents/fedgg.github.io/_notes"
DEST_ASSETS = "/Users/federico/Documents/fedgg.github.io/assets/images"
PUBLISH_TAG = "garden"  # Without the # since it's in YAML

def extract_frontmatter(content):
    """Extract YAML frontmatter and return it as dict, plus remaining content"""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        try:
            frontmatter_text = match.group(1)
            frontmatter_dict = yaml.safe_load(frontmatter_text)
            body = content[match.end():]
            return frontmatter_dict, body
        except:
            return None, content
    return None, content

def has_publish_tag(frontmatter_dict, body_content):
    """Check if note has the publish tag in YAML or body"""
    # Check in YAML tags
    if frontmatter_dict and 'tags' in frontmatter_dict:
        tags = frontmatter_dict['tags']
        if isinstance(tags, list):
            # Handle both "garden" and "#garden" in list
            if PUBLISH_TAG in tags or f"#{PUBLISH_TAG}" in tags:
                return True
        elif isinstance(tags, str):
            if PUBLISH_TAG in tags or f"#{PUBLISH_TAG}" in tags:
                return True

    # Check in body text
    if f"#{PUBLISH_TAG}" in body_content:
        return True

    return False

def clean_wikilinks(text):
    """Remove wikilink brackets from text"""
    if isinstance(text, str):
        # Remove [[wikilinks]] -> just the text inside
        return re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
    return text

def create_jekyll_frontmatter(original_frontmatter, filename):
    """Create Jekyll-compatible frontmatter with title, tags, and category"""
    # Start with title from filename if not present
    if not original_frontmatter or 'title' not in original_frontmatter:
        title = filename.replace('.md', '').replace('-', ' ').replace('_', ' ').title()
    else:
        title = original_frontmatter['title']

    # Create Jekyll frontmatter
    jekyll_fm = {'title': title}

    # Preserve tags (remove the publish tag from the list)
    if original_frontmatter and 'tags' in original_frontmatter:
        tags = original_frontmatter['tags']
        if isinstance(tags, list):
            # Remove publish tag and any #-prefixed versions, clean wikilinks
            tags = [clean_wikilinks(t).replace('#', '') for t in tags if t not in [PUBLISH_TAG, f"#{PUBLISH_TAG}"]]
            if tags:  # Only add if there are tags remaining
                jekyll_fm['tags'] = tags
        elif isinstance(tags, str):
            # Handle single tag as string
            tag_clean = clean_wikilinks(tags).replace('#', '')
            if tag_clean != PUBLISH_TAG:
                jekyll_fm['tags'] = [tag_clean]

    # Preserve category and strip wikilinks
    if original_frontmatter and 'category' in original_frontmatter:
        category = original_frontmatter['category']
        if isinstance(category, list):
            # Handle list of categories, clean wikilinks from each
            jekyll_fm['category'] = [clean_wikilinks(c) for c in category]
        else:
            # Single category, clean wikilinks
            jekyll_fm['category'] = clean_wikilinks(category)

    # Preserve date if present
    if original_frontmatter:
        if 'date' in original_frontmatter or 'Date' in original_frontmatter:
            jekyll_fm['date'] = original_frontmatter.get('date') or original_frontmatter.get('Date')

    # Convert to YAML string
    fm_text = "---\n"
    for key, value in jekyll_fm.items():
        if isinstance(value, list):
            fm_text += f"{key}:\n"
            for item in value:
                fm_text += f"  - {item}\n"
        else:
            fm_text += f"{key}: {value}\n"
    fm_text += "---\n\n"

    return fm_text

def convert_wikilinks(content):
    """Convert [[wikilinks]] to [wikilinks](wikilinks.md)"""
    def replace_note_link(match):
        link_text = match.group(1)

        # Skip if it's a folder reference like [[Concepts]]
        if link_text.startswith('AllNotes/') or '/' in link_text:
            # Extract just the note name after the last /
            parts = link_text.split('/')
            if '|' in parts[-1]:
                target, display = parts[-1].split('|', 1)
            else:
                target = display = parts[-1]
        elif '|' in link_text:
            target, display = link_text.split('|', 1)
        else:
            target = display = link_text

        # Convert to lowercase, replace spaces with hyphens
        filename = target.lower().replace(' ', '-') + '.md'
        return f"[{display}]({filename})"

    content = re.sub(r'\[\[([^\]]+)\]\]', replace_note_link, content)
    return content

def convert_image_links(content, note_path):
    """Convert ![[image.jpg]] to ![image](/assets/images/image.jpg) and copy images"""
    def replace_image(match):
        image_name = match.group(1)

        # Find image in assets folder relative to note
        note_dir = Path(note_path).parent

        # Look for assets folder in the same directory as the note
        source_image = note_dir / "assets" / image_name

        # If not found, try looking in parent directories (up to 2 levels)
        if not source_image.exists():
            source_image = note_dir.parent / "assets" / image_name
        if not source_image.exists():
            source_image = note_dir.parent.parent / "assets" / image_name

        if source_image.exists():
            # Copy to destination assets
            dest_image = Path(DEST_ASSETS) / image_name
            dest_image.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_image, dest_image)
            print(f"  ✓ Copied image: {image_name}")
            print(f"    From: {source_image}")
        else:
            print(f"  ⚠ Image not found: {image_name}")
            print(f"    Searched in: {note_dir / 'assets'}")

        # Return Jekyll-compatible markdown
        return f"![{image_name}](/assets/images/{image_name})"

    content = re.sub(r'!\[\[([^\]]+\.(jpg|jpeg|png|gif|svg|webp|JPG|JPEG|PNG|GIF|SVG|WEBP))\]\]', replace_image, content)
    return content


def sync_notes():
    """Main sync function"""
    print(f"\n🌱 Syncing Digital Garden from {SOURCE_VAULT}")
    print(f"   Publishing notes tagged with '{PUBLISH_TAG}'\n")

    # Clear existing notes
    if os.path.exists(DEST_NOTES):
        shutil.rmtree(DEST_NOTES)
    os.makedirs(DEST_NOTES, exist_ok=True)

    # Ensure assets directory exists
    os.makedirs(DEST_ASSETS, exist_ok=True)

    synced_count = 0

    # Walk through source vault
    for root, dirs, files in os.walk(SOURCE_VAULT):
        for filename in files:
            if not filename.endswith('.md'):
                continue

            source_path = os.path.join(root, filename)

            # Read note content
            try:
                with open(source_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                print(f"⚠ Could not read: {filename}")
                continue

            # Extract frontmatter
            frontmatter_dict, body = extract_frontmatter(content)

            # Check for publish tag
            if not has_publish_tag(frontmatter_dict, body):
                continue

            print(f"📝 Processing: {filename}")

            # Create Jekyll frontmatter
            jekyll_frontmatter = create_jekyll_frontmatter(frontmatter_dict, filename)

            # Process body content
            body = convert_image_links(body, source_path)
            # body = convert_wikilinks(body) # Let Jekyll handle wikilinks

            # Combine frontmatter and body
            final_content = jekyll_frontmatter + body

            # Write to destination
            dest_path = os.path.join(DEST_NOTES, filename)
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(final_content)

            synced_count += 1
            print(f"  ✓ Synced to: {filename}\n")

    print(f"\n✅ Sync complete! {synced_count} notes published.\n")
    print("Next steps:")
    print("  1. Check http://localhost:4000 to preview")
    print("  2. Run: git add . && git commit -m 'Updated garden' && git push")

if __name__ == "__main__":
    sync_notes()
    
