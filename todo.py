#!/usr/bin/env python3

import os
import datetime
import subprocess
import shutil

from os.path import expanduser

TODO_DIR = expanduser("~/todos/")
TODO_PREFIX = "TODO-"
EDITOR = expanduser("~/bin/sublime_text")

os.makedirs(TODO_DIR, exist_ok=True)
os.chdir(TODO_DIR)

now = datetime.datetime.now()
today_file = "%s%s-%s-%s" % (TODO_PREFIX, now.year, now.month, now.day)

# find most recent (by last modified date) TODO file
most_recent_file = subprocess.run(['ls', '-1tr'], stdout=subprocess.PIPE).stdout.decode().strip('\n').split('\n')[-1]

if not most_recent_file:
    print('Dir was empty, new file will be created')
elif today_file != most_recent_file:
    print('Most recent file was %s, copying to %s' % (most_recent_file, today_file))
    shutil.copyfile(most_recent_file, today_file)
else:
    print("Today's file is most recent (%s), opening" % (today_file))

with open(os.devnull, 'w') as fp:
    subprocess.Popen([EDITOR, today_file], stdout=fp, stderr=fp)
