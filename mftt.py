#!/bin/python3

import re
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
from os import get_terminal_size

tabs = 2
columns, rows = get_terminal_size()
vr = '\033[90m|\033[0m'
language = ''
hr_template = ' \033[90m{} {}\033[0m'
is_colored_code = False

# Función para retornar código coloreado
def colored_code(code_line):
    return highlight(code_line, PythonLexer(), TerminalFormatter()) if language == 'py' else code_line

def colored_comment(code_line):    
    spaces = ' ' * (abs(columns - len(code_line)) - 3)

    if re.search('^(\#\s.+)$', code_line):
        code_line = f'\033[3;90m{code_line}\033[0m'
    elif re.search('(.+)?(\#\s.+)', code_line):
        code, comment = re.findall('(.+)?(\#\s.+)', code_line)[0]
        code_line = colored_code(code).rstrip() + f'\033[3;90m{comment}\033[0m'
    else:
        code_line = colored_code(code_line).rstrip()
    
    return '{} {}{}{}'.format(vr, code_line, spaces, vr)

def open_md(filepath):
    with open(filepath) as file:
        for line in file.readlines():
            global is_colored_code, language
            line = line.replace('\t', ' ' * tabs).rstrip()
            spaces = ' ' * (abs(columns - len(line)) - 3)

            if re.search('^\`\`\`$', line):
                line = hr_template.format(language, hr)
                is_colored_code = False
            elif re.search('^\`\`\`\w+$', line):
                language = re.findall('^\`\`\`(\w+)$', line)[0]
                hr = "-" * (columns - 3 - len(language))
                line = hr_template.format(hr, language)
                is_colored_code = True
            elif is_colored_code:
                line = colored_comment(line)
            else:
                # Títulos
                line = re.sub('^(\#{1,6}) (.+)', r'\033[1;96m\2\033[0m', line)
                # Lista: Ordenada
                line = re.sub('^(\d+(\.|\)))', r' \033[90m\1\033[0m', line)
                # Lista: Desordenada
                line = re.sub('^(\s{1,})?([-+*])(\s.+)', r' \1•\3', line)
                # Negrita
                line = re.sub('\*\*(.*?)\*\*', r'\033[1m\1\033[0m', line)
                # Italica
                line = re.sub('\_(.*?)\_', r'\033[3m\1\033[0m', line)
                # Subrayado
                line = re.sub('<u>(.+)</u>', r'\033[4m\1\033[0m', line)
                # Texto centrado
                if re.search('<center>(.+)</center>', line):
                    line = re.sub('<center>(.+)</center>', r'\1', line)                    
                    spaces = re.findall('^\s+', re.sub('\\033\[.*?m', '', line).center(columns))[0]
                    line = spaces + line
                # Texto a la derecha
                if re.search('<\w*\s(.{1,})?align="right"(.{1,})?>.+</\w*>', line):
                    line = re.sub('<\w*\s(.{1,})?align="right"(.{1,})?>(.+)</\w*>', r'\3', line)
                    spaces = re.findall('^\s+', re.sub('\\033\[.*?m', '', line).rjust(columns))[0]
                    line = spaces + line
            # Salida
            print(line)

if __name__ == '__main__':
    open_md('./tuplas.md')
