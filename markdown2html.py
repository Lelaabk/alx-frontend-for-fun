#!/usr/bin/python3
"""
This is a script to convert a Markdown file to HTML.

Usage:
    ./markdown2html.py [inputf] [outputf]

Arguments:
    inputf: the name of the Markdown file to be converted
    outputf: the name of the output HTML file

Example:
    ./markdown2html.py README.md README.html
"""

import argparse
import pathlib
import re
import sys


def md_to_html(inputf, outputf):
    '''
    Converts markdown file to HTML file
    '''
    # Read the contents of the input file
    with open(inputf, encoding='utf-8') as f:
        markd_text = f.readlines()

    html_content = []
    for line in markd_text:
        # Check if the line is a heading
        match = re.match(r'(#){1,6} (.*)', line)
        if match:
            # Get the level of the heading
            h_level = len(match.group(1))
            # Get the content of the heading
            h_content = match.group(2)
            # Append the HTML equivalent of the heading
            html_content.append(f'<h{h_level}>{h_content}</h{h_level}>\n')
        else:
            html_content.append(line)

    # Write the HTML content to the output file
    with open(outputf, 'w', encoding='utf-8') as f:
        f.writelines(html_content)


if __name__ == '__main__':
    # Parse command-line arguments
    prs = argparse.ArgumentParser(description='Convert markdown to HTML')
    prs.add_argument('inputf', help='path to input markdown file')
    prs.add_argument('outputf', help='path to output HTML file')
    args = prs.parse_args()

    # Check if the input file exists
    input_path = pathlib.Path(args.inputf)
    if not input_path.is_file():
        print(f'Missing {input_path}', file=sys.stderr)
        sys.exit(1)

    # Convert the markdown file to HTML
    md_to_html(args.inputf, args.outputf)