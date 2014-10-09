#!/usr/bin/python
import urllib2
import bs4
import os
from bs4 import BeautifulSoup

def getLinks(soup,file):
   for tags in soup.find_all('a'):
         if 'href' in tags.attrs and 'http' in tags['href']:
            try:
               file.write(tags['href']+"\n")
              # print tags['href']
            except UnicodeEncodeError:
               pass
count=0            
URI="null"
links = open('unique_links.dat','r')
while count < 50 and URI:
   URI=links.readline().rstrip('\n')
   if URI:
      try:
         response = urllib2.urlopen(URI)
         http = response.read()
         response.close()
         bsoup = BeautifulSoup(http)
         cmd = 'echo "' + URI + '" | md5sum | tr -d "  -"'
         hash = os.popen(cmd).read().rstrip('\n')
         hash="./URIlinks/" + hash
         print str(count) + " " + hash
         file=open(hash,'w')
         file.write("site:\n" + URI + "\nlinks:\n")
         getLinks(bsoup,file)
         file.close()
         count = count + 1;
      except urllib2.HTTPError and urllib2.URLError:
         pass
