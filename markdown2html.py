#!/usr/bin/python3
import sys
import os
import markdown


def markdown_to_html(input_f, output_f):
    """Convert Markdown file to HTML file."""
    with open(input_f, "r") as f:
        md_text =  f.read()
    html_text = markdown.markdown(md_text)
    with open(output_f, 'w') as f:
        f.write(html_text)

def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
        sys.exit(1)
        input_f = sys.argv[1]
        output_f = sys.argv[2]
        if not os.path.exists(input_f):
            sys.stderr.write(f"Missing {input_f}\n")
            sys.exit(1)

        markdown_to_html(input_f, output_f)
        sys.exit(0)
    
    if __name__ == "__main__":
    main()