#!/bin/python3

from sys import argv
from mftt import open_md

files = argv[1:]

for file in files:
    open_md(file)
