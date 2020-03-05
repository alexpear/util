#!/usr/bin/python

import datetime
import os
import shutil
import sys

def backup(filepaths):
    # arg is relative path to what we want to backup
    if len(filepaths) < 1:
        print('usage: backup filepath...')
        return

    # TODO: Ability to fail one filename without ceasing whole script.
    # check the relative path(s) are legit
    for filepath in filepaths:
        if not os.path.exists(filepath):
            print('error: couldnt find "{file}", relative to current directory'.format(file=filepath))
            return

    dt = datetime.datetime.now()

    yearstr = "{year:04}".format(year=dt.year)
    datestr = "{month:02}{day:02}".format(month=dt.month, day=dt.day)
    timestr = "{hour:02}{minute:02}".format(hour=dt.hour, minute=dt.minute)

    # do dirs corresopnding to today's date exist?
    backups_path = os.path.expanduser('~/backups/')

    if not os.path.isdir(backups_path + yearstr):
        os.mkdir(backups_path + yearstr)

    date_path = backups_path + yearstr + '/' + datestr + '/'
    if not os.path.isdir(date_path):
        os.mkdir(date_path)

    desired_path = date_path + timestr + '/'
    if not os.path.isdir(desired_path):
        os.mkdir(desired_path)

    for filepath in filepaths:
        if os.path.exists(desired_path + os.path.basename(filepath)):
            # TODO: Instead, do back it up with a incremented filename
            # if already exists in backups dir...
            print('ERROR: file "{file}" already backed up here, not overwriting'.format(file=filepath))
            return
        else:
            shutil.copy(filepath, desired_path)
            print('copying {file}'.format(file=os.path.basename(filepath)))

    print('backup complete thank you :)')

backup(sys.argv[1:])
