#!/usr/bin/python3
import sys
import os


def markdown_to_html(markdown_f, output_f):
    """Convert Markdown file to HTML file."""
    if not os.path.exists(markdown_f):
        print(f"Missing {markdown_f}", file=sys.stderr)
        sys.exit(1)
    with open(markdown_f, "r") as f:
        md_text =  f.read()
    with open(output_f, 'w') as f:
        f.write(md_text)

def main():
    """Main function to parse command line args and convert Markdown to HTML"""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    markdown_f = sys.argv[1]
    output_f = sys.argv[2]
    
    markdown_to_html(markdown_f, output_f)
    sys.exit(0)    

if __name__ == "__main__":
    main()
