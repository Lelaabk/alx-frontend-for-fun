#!/usr/bin/python3
import sys
import os
import re


# This check for command line args
if len(sys.argv) == 1:
    sys.exit(1)

# This check if input file exists
if not os.path.isfile(sys.argv[1]):
    sys.exit(2)

# Inpit and output file names
inputf = sys.argv[1]
outputf = re.sub(r'\.(md|markdown)$', '', inputf)+'.html'

inputf = open(inputf, 'r') 
ifile_str = inputf.read() + '\n'
outputf = open(outputf, 'w') 
ofile_str = ''

# Initialize boolean flags & counters
B = False  # bold
I = False  # italic
S = False  # strikethrough
c = 0      # code
C = False  # Code block
Q = 0      # Block quote
p = False  # Paragraph 
i = 0

# Loop through the string
while i < len(ifile_str)-2:
    str = ifile_str[i]
    i += 1

    # Open paragraph tag if not open
    if str != '\n' and not pr:
        outputf.write('<p>')
        pr = True

    # Handle bold & italic syntax
    if str in ('*', '_'):
        if C:
            outputf.write(str)
            continue
        if ifile_str[i] in ('*', '_'):
            outputf.write(f'<{"/"*B}b>')
            B = not B
            i += 1
        else:
            outputf.write(f'<{"/"*I}i>')
            I = not I

    # Handle code syntax
    elif str == '`':
        str_b, str_c = ifile_str[i], ifile_str[i+1]
        if str == str_b == str_c:
            outputf.write(f'<{"/"*C}code>')
            C = not C
            i += 2
        else:
            if C:
                outputf.write(str)
                continue
            outputf.write(f'<{"/"*c}code>')
            c = not c

   # Handle strike syntax 
    elif str == '~':
        if C:
            outputf.write(str)
            continue
        if ifile_str[i] == '~':
            outputf.write(f'<{"/"*S}del>')
            S = not S
            i += 1

    # Handle horizontal rule syntax
    elif str in ('-', '*', '_'):
        str_b , str_c = ifile_str[i], ifile_str[i+1]
        if ((i > 1 and ifile_str[i-2] == '\n') or i == 1) and ifile_str[i+2] == '\n':
            if str == str_b == str_c:
                if B:
                    outputf.write(f'</b>')
                    B = False
                if I:
                    outputf.write(f'</i>')
                    I = False
                if S:
                    outputf.write(f'</del>')
                    S = False
                outputf.write('<hr>')

    # Handle line syntax
    elif str == '[':
        if re.match('^\[.*\]\(.*(".*"|)\)$', ifile_str[i-1:].split(')',1)[0]+')'):
            name = ''
            link = ''
            alt = ''
            s = ifile_str[i:].split(')',1)[0]+')'
            i += len(s)
            name = s.split(']')[0]
            link = s.split('(')[1].split(')')[0]
            if '"' in link:
                alt = link.split('"')[1].split('"')[0]
                link = link.split('"')[0].strip()
            outputf.write(f'<a href="{link} title="{alt}">{name}</a>')

    # Handle new line
    elif str == '\n':
        if C:
            outputf.write(str)
            continue

        if c:
            outputf.write(f'</code>')

        if not p:
            outputf.write('<br>')
        elif ifile_str[i] == '\n':
            outputf.write('</p>\n')
            p = False
            i += 1

            if B:
                outputf.write(f'</b>')
                B = False
            if I:
                outputf.write(f'</i>')
                I = False
            if S:
                outputf.write(f'</del>')
                S = False
        elif not ifile_str[i]:
            if p:
                outputf.write('</p>\n')
            else:
                outputf.write('\n')
        else:
            outputf.write('<br>')

        outputf.write('\n')

    else:
        outputf.write(str)

# Close input & output files
inputf.close()
outputf.close()
