import sys
import urllib2
import bs4
import time
from bs4 import BeautifulSoup

school=sys.argv[1]
timesleep=sys.argv[2]
URI=sys.argv[3]

def getTRparent(element):
        for parent in element.parents:
                if parent.name == "tr":
                        return parent

        print "Error no tr found."
        return "error"

#get the html representation from the provided
# URI and use BeautifulSoup to parse it
#response = urllib2.urlopen("http://sports.yahoo.com/college-football/scoreboard/?week=2&conf=all")

while True:
	response = urllib2.urlopen(URI)
	http = response.read()
	response.close()
	soup = BeautifulSoup(http)

	trlist = []

	#find team or possible teams and store their base tag 'tr' in a list
	for tags in soup.find_all('em'):
	        if school in tags.contents:#format the contents and string so they are lower case
        	        trlist.append(getTRparent(tags))

	#condense this bullshit store home, away, and scores for later use: 
	for tr in trlist:
	        for child in tr.children:
        	        if isinstance(child,bs4.element.Tag):
                	        if "class" in child.attrs and "away" in child['class']:
                        	        for element in child.children:
                                	        if isinstance(element,bs4.element.Tag) and "team" in element['class']:
                                        	        print "away: " + element.em.string
				elif "class" in child.attrs and "score" in child['class']:
                        	        for element in child.h4.a.children:
                                	        if isinstance(element,bs4.element.Tag) and "away" in element['class']:
                                        	        print "away score: " + element.string

	                                        if isinstance(element,bs4.element.Tag) and "home" in element['class']:
        	                                        print "home score: " + element.string

	                        elif "class" in child.attrs and "home" in child['class']:
        	                        for element in child.children:
                	                        if isinstance(element,bs4.element.Tag) and "team" in element['class']:
							print "home: " + element.em.string
	#timesleep=timesleep + 0.0 #convert to float
	print
	time.sleep(float(timesleep))
