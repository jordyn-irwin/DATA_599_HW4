#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys
import re
  
for line in sys.stdin: 
    line = re.sub("[^A-Za-z]","", line).strip() 
    words = line.split() 
    for word in words:
        print('%s\t%s' % (word, 1))
