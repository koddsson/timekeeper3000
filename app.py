#!/usr/bin/python
# -*- coding: latin-1 -*-
import os
import sys
import argparse
from datetime import datetime

# For the popup
from psidialogs import ask_string as GetText

from modules.twitter_module import TwitterModule
from modules.webcam_module import WebcamModule

module_list = [
    TwitterModule(),
    WebcamModule()
    ]

ship_log = True

parser = argparse.ArgumentParser(description='Stuff, I guess')
parser.add_argument('output', metavar='OUTPUT_FILE',
                    type=argparse.FileType('a+b'), help="output file")
args = parser.parse_args()
f = vars(args)['output']

# There must be a better way to get last message
last_message = ""
if os.path.getsize(f.name) > 0:
    last_message = f.readlines()[-1].split('>')[1].strip()

# Get the work being done
text = GetText("What's going on?", last_message)

# Get the date after the popup so that we get
# the timestamp on the time of writing.
d = datetime.now().strftime("%Y-%m-%d %H:%M")

# Write the instance to the log
f.write("[%s] > %s\n" % (d, text))
f.close()

for module in module_list:
    if not module.activate(status=text):
        print 'Module %s like totally failed' % module

if ship_log is False:
    sys.exit(0)
