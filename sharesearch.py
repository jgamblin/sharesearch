#!/usr/bin/env python
# Name:     sharesearch.py
# Purpose:  Searches Shares For Keywords
# By:       Jerry Gamblin
# Date:     16.07.15
# Modified  16.08.15
# Rev Level 0.1
# -----------------------------------------------

import os
import sys
import re

output = open('output.txt', 'a')
output.write('\n')

filelist = []
sharelist = open('shares.txt', 'r')

eachshare = sharelist.readlines();

for shares in eachshare:
    path = shares.rstrip('\r\n')
    print ('\n''Walking directory  ' + path + ' \n')
    for root, dirs, files in os.walk(path):
        print ('Indexing ' + root + ' \n ')
        for file in files:
            filelist.append(os.path.join(root,file))
            print ('Found ' + root + file)

keywords = open('searchterms.txt', 'r')
searchterm = keywords.readlines();

output.write('=== Directories or file names matching search criteria ===\n')

for term in searchterm:
    strip = term.rstrip('\r\n')
    if any(strip in s for s in filelist):
        matching=[s for s in filelist if strip in s]
        for item in matching:
            output.write('\n' + item)
output.write('\n\n=== Files matching search criteria ===\n\n')
for term in searchterm:
    strip = term.strip('\r\n')
    for item in filelist:
        print 'Searching file ' + item + ' for term ' + term
        searchfile = open(item, 'rb')
        for line in searchfile:
            if re.search(strip, line, re.IGNORECASE):
                output.write('found ' + strip + ' in file ' + item + '\n')
                break
        searchfile.close()
output.close()
