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
