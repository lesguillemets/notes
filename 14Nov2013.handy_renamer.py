#!/usr/bin/python3

import re
import os

pattern = re.compile(r'([^_]*)_.*') # pattern to match.
files = [f for f in os.listdir('.') if os.path.isfile(f)
                          and f[-4:] == '.mp3'] # mp3 files under ./

for f in files:
    if not pattern.match(f):
        print("skipping {}".format(f))
        continue
    newname = pattern.sub(lambda x: x.group(1) + ".mp3", f) # basename.mp3
    if os.path.exists(newname):
        confirm = input("{} already exists. override? [y/n]"
                        .format(newname)) # prompt before overriding
        if confirm != 'y':
            continue
    os.rename(f, newname)

print("done.")
