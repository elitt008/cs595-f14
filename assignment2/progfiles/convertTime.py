#!/usr/bin/python
import time
import fileinput
import sys

datesampled=time.strptime("2014-09-27T06:00:00","%Y-%m-%dT%H:%M:%S")
for line in sys.stdin:#fileinput.input():
   line = line.rstrip()
   newtime=time.strptime(line,"%Y-%m-%dT%H:%M:%S")
   diffsec= time.mktime(datesampled) - time.mktime(newtime)
   diffhour = diffsec / 3600 
   print int(diffhour)
