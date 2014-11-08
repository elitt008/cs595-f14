#!/usr/bin/python
from igraph import *

karate = Graph.Read_GraphML("karate.GraphML")

count=1
list1=[]
print "{\n\"nodes\":["
for element in karate.vs:
   print "{\"actor\": \"" + element['name']+ "\", \"faction\": " + str(element['Faction']) + "},"
print "],"
for name in karate.vs["name"]:
   if "Actor" in name:
      list1.append(str(count))
   else: 
      list1.append(name)
   count = count + 1
karate.vs["label"]=list1

