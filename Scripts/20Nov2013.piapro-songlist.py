#!/usr/bin/python3
# coding:utf-8

import urllib.request
import re
import time

usr = "YOUR_WANTED_USER_ID"

base_address = "http://piapro.jp/content_list/?pid={}&view=audio".format(usr)

tpattern = re.compile(r'<td class="title"><a href=".+">(.*)</a></td>')
lpattern = re.compile(r'<td class="time">([0-9 :]+)</td>')

titles = [] # list of the titles
lengths = [] # list of the corresponding durations.
count = 0 # how many songs have we checked?

with urllib.request.urlopen(base_address + "&start_rec={}".format(count)) as u:
    htmltext = u.read().decode("utf-8") # fetch html.

ttls = tpattern.findall(htmltext) # list of the titles in the current buffer.
lnts = lpattern.findall(htmltext) # list of the corresponding lengths.

if len(ttls) == 0:
    break # stop when all the uploads are checked.

titles += ttls # add to database
lengths += lnts

print("fetching songs from No.{}, this is the {} th request...".format(count, n))
# yes, I know how irritating it is to see these expressions like "1 th".....
count += len(ttls)
time.sleep(5) # this should be long enough.

print(list(zip(titles,lengths)))

# save to file
with open("songs.txt", 'a') as f:
    for (i,title) in enumerate(titles):
        f.write("{}\t{}\n".format(title, lengths[i]))
