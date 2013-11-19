#!/usr/bin/python3
# coding:utf-8

from songs import songs

import subprocess as sub
from os.path import expanduser


def str_to_secs(tst):
    # "02:10" => "130"
    return str(int(tst[:2])*60 + int(tst[3:]))

dirpath = expanduser("~/Music/songs_to_check/")

for (title, length) in songs:
    filename = (dirpath + title + ".mp3")
    # ~/Music/songs_to_check/title.mp3
    try:
        actual_length = (sub.check_output(["mp3info", "-p", '"%S"', filename]).
                                  decode("utf-8").strip('"'))
        # $ mp3info -p "%S" filename # => 139
        # sub.check_output([******]).decode("utf-8") # => '"139"'
        # _.strip('"') # => '139'
    except:
        # if mp3info failed for some reason
        print("\033[104mSkip\033[0m {}".format(title))
        continue

    if str_to_secs(length) != actual_length:
        # these files should be broken
        print("\033[101mWARNING\033[0m {}\t : \
              should be {} secs long, while this file is {} secs long."
              .format(title, str_to_secs(length), actual_length))
    else:
        # if the lengths match
        print("\033[102mMatch\033[0m {}\t : \
              both {} long".format(title, actual_length))
