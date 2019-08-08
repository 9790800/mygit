#!/bin/python3

import os
script = 'ls -lah /home'
os.system("bash -c '%s'" % script)
