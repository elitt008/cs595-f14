#!/usr/bin/python
import urllib2
import time

uniqlinks = open('unique_links.dat','r')
file=open("mementos.dat",'w')

line="null"
count=0
while line :
   line = uniqlinks.readline().rstrip('\n')
   if line:
      print line
      try:
         response=urllib2.urlopen("http://mementoweb.org/timemap/link/" + line)
         mementos=response.read()
         memcount= mementos.count('rel="memento"')
         file.write(str(memcount)+","+line+"\n") 
         print "opened" + str(count)
         response.close()
      except:# ZeroDivisionError:
         file.write("0,"+line+"\n")
         print "passed" + str(count)
         pass
      count=count+1
      print count   
file.close()   
uniqlinks.close()
