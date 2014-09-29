#!/usr/bin/python
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs

import json
from pprint import pprint
import time
import re
import urllib2
import httplib

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "QX9UsnHmngd6vD20LgEBXtvoN"
CONSUMER_SECRET = "Kkvt4i7x2pglyl8qhSlzdoHc2vjexNlrW8xGNZZeaFY2QjavQx"

OAUTH_TOKEN = "2825370151-dNfwsYgzC12FUyZjM4MhoXu4D7hMmG1RguUd3q0"
OAUTH_TOKEN_SECRET = "pZV2GtrPOPG9v3V0ugTWYqgm0KpyKrGlFQTj5djQu5I8C"


def get_oauth():
	oauth = OAuth1(CONSUMER_KEY,
	client_secret=CONSUMER_SECRET,
	resource_owner_key=OAUTH_TOKEN,
	resource_owner_secret=OAUTH_TOKEN_SECRET)
	return oauth

oauth = get_oauth()
frontend="https://api.twitter.com/1.1/search/tweets.json?q="
backend=" filter%3Alinks&src=typd&count=100"
searchlist=['breaking news','Syria','ISIS','NFL','Putin','computer science','internet','geology','Obama',
'physics','math','NASA','The Strokes','MIT','computers','AMD',
'Intel','Bethesda','Star Wars']

i=0
uniqLinks=set()
while len(uniqLinks) < 1000 and i < len(searchlist):
   r = requests.get(url=frontend+searchlist[i]+backend, auth=oauth)
   json_data=r.json()
   i=i+1
   for element in json_data['statuses']:
      if len(uniqLinks) < 1000:
         try:
            URL= re.search("(?P<url>https?://[^\s]+)", element['text']).group("url")
            resource = urllib2.urlopen(URL)
            finalURL = resource.geturl()
            resource.close()
            print URL
            print finalURL 
            uniqLinks.add(finalURL)
         except:
            pass
   print len(uniqLinks)
   print i

file = open('unique_links.dat','w')
for link in uniqLinks:
   file.write(link+"\n")
file.close()
