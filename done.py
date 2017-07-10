#!/usr/bin/env python3

import os
import sys
from os.path import expanduser, isfile, join

TODO_DIR = expanduser("~/todos/")
TODO_PREFIX = "TODO-"

os.chdir(TODO_DIR)

todo_files = [f for f in os.listdir(TODO_DIR) if isfile(join(f))]

if len(sys.argv) > 1:
    start = 'TODO-'+sys.argv[1]
    todo_files = [todo_file for todo_file in todo_files if todo_file >= start]


if len(sys.argv) > 2:
    end = 'TODO-'+sys.argv[2]
    todo_files = [todo_file for todo_file in todo_files if todo_file <= end]

for todo_file in todo_files:
    with open(todo_file) as f:
        in_done = False
        things_done = []

        for line in f:
            if in_done:
                things_done.append(line.strip().strip('\n\t '))
            elif line.startswith('DONE'):
                in_done = True

    if things_done:
        print(todo_file + ':')
        for thing in things_done:
            print('\t' + thing)
        print()
