#!/usr/bin/python3

# ONLY for Mac OSX

import os
import sys

def trash (name):
    if os.path.exists(name):
        os.system(
            'osascript -e \'tell app "Finder" to move the POSIX file "'
            + os.path.abspath(name)
            + '" to trash\''
        )
    else:
        print('error: ' + os.path.abspath(name) + ' does not exist')

# run cli script
if sys.platform != 'darwin':
    print('error: this script only supports Mac OSX darwin')
elif len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        trash(arg)
else:
    print('usage: trash [file...]')
    print('  move file(s) to OSX Trash')
