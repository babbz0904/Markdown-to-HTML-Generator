Markdown Parsing and Block Extraction:

Implemented functions to extract blocks from Markdown text, such as markdown_to_blocks.
Defined block types like headings, paragraphs, code blocks, lists, quotes, etc.
Created functions to identify block types, such as block_to_block_type.
HTML Node Representation:

Defined classes to represent HTML nodes, such as HTMLNode, LeafNode, and ParentNode.
Implemented methods to convert HTML nodes to HTML strings, like to_html.
Markdown to HTML Conversion:

Developed functions to convert Markdown blocks to HTML nodes, like markdown_block_to_html_node.
Created a function to convert a full Markdown document to HTML nodes, such as markdown_to_html_nodes.
Template Rendering:

Designed a function to render Markdown content into an HTML template, such as render_template.
File Operations:

Implemented functions to read Markdown and HTML template files, such as read_markdown_file and read_template_file.
Developed functions to write generated HTML content to files, like write_html_to_file.
Directory Crawling and Page Generation:

Developed a recursive function to generate HTML pages from Markdown files in a directory structure, like generate_pages_recursive.
Implemented a function to generate a single HTML page from a Markdown file, such as generate_page.
Main Functionality:

Created a main function to orchestrate the Markdown to HTML conversion process, like main.
CLI Interface:

Provided command-line interface functionality using argparse to specify input and output directories, templates, etc.
Error Handling:

Implemented error handling for file reading, writing, and other operations.
Added logging to track progress and errors during the conversion process.
