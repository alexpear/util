#!/usr/bin/env python

# ONLY for Mac OSX

import os
import sys

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if os.path.exists(arg) and (sys.platform == 'darwin'):
            os.system('osascript -e \'tell app "Finder" to move the POSIX file "'
            	+ os.path.abspath(arg) + '" to trash\'')
        else:
            print 'Error: ', os.path.abspath(arg), ' does not exist'
else:
    print 'usage: trash [file...]'
    print '  move file(s) to OSX Trash'
