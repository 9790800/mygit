import os
script = 'ls -lah /home'
os.system("bash -c '%s'" % script)