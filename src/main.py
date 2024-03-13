from textnode import TextNode
from markdown_blocks import markdown_to_blocks, block_to_block_type, block_type_heading, markdown_to_html_node
from pathlib import Path
import os
import shutil

def copy_directory_contents(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Iterate over all items (files and directories) in the source directory
    for item in os.listdir(source_dir):
        # Form the full paths of the source and destination items
        source_item_path = os.path.join(source_dir, item)
        destination_item_path = os.path.join(destination_dir, item)
        
        # If the item is a file, copy it to the destination
        if os.path.isfile(source_item_path):
            shutil.copy(source_item_path, destination_item_path)
            print(f"Copied file: {source_item_path} -> {destination_item_path}")
        # If the item is a directory, recursively copy its contents
        elif os.path.isdir(source_item_path):
            copy_directory_contents(source_item_path, destination_item_path)

# Test the function by copying contents of "static" directory to "public" directory
source_directory = "static"
destination_directory = "public"

# Delete contents of the destination directory if it already exists
if os.path.exists(destination_directory):
    shutil.rmtree(destination_directory)

# Copy contents of the source directory to the destination directory
copy_directory_contents(source_directory, destination_directory)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == block_type_heading and block.startswith("# "):
            return block[1:].strip()
        
    raise Exception

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read markdown file
    with open(from_path, 'r') as file:
        markdown_content = file.read()

    # Convert markdown to HTML
    html_content = markdown_to_html_node(markdown_content).to_html()

    # Extract title
    title = extract_title(markdown_content)

    # Read template file
    with open(template_path, 'r') as file:
        template_content = file.read()

    # Replace placeholders with HTML and title
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_content)

    
    dest_directory = os.path.dirname(dest_path)
    os.makedirs(dest_directory, exist_ok=True)

    # Write HTML to file
    with open(dest_path, 'w') as file:
        file.write(template_content)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, _, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):
                markdown_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(markdown_file_path, dir_path_content)
                dest_file_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + '.html')
                generate_page(markdown_file_path, template_path, dest_file_path)

        
generate_pages_recursive('content', 'template.html', 'public')