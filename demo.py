#!/bin/python3

import os
from simple_term_menu import TerminalMenu
from string import ascii_lowercase
from mftt import open_md

DIR_DOCS='./docs'

options = [ filename for filename in os.listdir(DIR_DOCS) if filename.endswith('.md') ]
optionsListed = [ f'[{ascii_lowercase[index]}] {item}' for index, item in enumerate(options) ]
optionsListed.append("[q] Quit")

mainMenu = TerminalMenu(optionsListed)

quitting = False

while quitting == False:
    optionIndex = mainMenu.show()

    if (optionsListed[optionIndex] == optionsListed[-1]):
        quitting = True
    else:
        open_md(os.path.join(DIR_DOCS, options[optionIndex]))
        quitting = True
