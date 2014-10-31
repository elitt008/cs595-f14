#!/usr/bin/python
from igraph import *

karate = Graph.Read_GraphML("karate.GraphML")
summary(karate)
print karate.vs
layout=karate.layout_kamada_kawai()
plot(karate,layout=layout)
#for element in karate.vs["name"]:
#   print element
#for element in karate.vs["Faction"]:
#   print element
print type(karate.es["weight"])
#count=0
#for element in karate.es["weight"]:
#   print count," ",element
#   count=count+1
#count=1
edgebetweenesslist = karate.edge_betweenness()
#for element in betweenesslist:
#   print count," ", element
#   count = count + 1

#vertexbs=karate.community_edge_betweenness(weights=karate.es["weight"]).as_clustering(n=2)
#for element in vertexbs:
#   print type(element)
#   count=1
#   for element1 in element:
#      print count," ",element1
#      count = count + 1 
count=1
bs=karate.community_leading_eigenvector(clusters=2,weights=karate.es["weight"])


for element1 in bs:
   summary(element1)
#   for element2 in element1:
      

   print count," ",element1
   count = count + 1 



#g=bs.cluster_graph()
#layout=g.layout_kamada_kawai()
#plot(g,layout=layout)
#print karate.community_edge_betweenness(directed=False)
#print karate.community_edge_betweenness(directed=False,clusters=5)
#print karate.community_edge_betweenness(directed=False,clusters=5,weights=karate.es["weight"])
#print karate.community_edge_betweenness(directed=False)
#print karate.community_edge_betweenness(directed=False,clusters=5)
#print karate.community_edge_betweenness(directed=False,clusters=5,weights=karate.es["weight"])
