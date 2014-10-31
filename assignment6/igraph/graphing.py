#!/usr/bin/python
from igraph import *

karate = Graph.Read_GraphML("karate.GraphML")
summary(karate)

count=1
list1=[]
for name in karate.vs["name"]:
   if "Actor" in name:
      list1.append(str(count))
      #print name
      #print karate.vs["label"][count]
   else: 
      list1.append(name)
   count = count + 1
#print list1
karate.vs["label"]=list1
#print karate.vs["label"]

bs2=karate.community_leading_eigenvector(clusters=2,weights=karate.es["weight"])
bs3=karate.community_leading_eigenvector(clusters=3,weights=karate.es["weight"])
bs4=karate.community_leading_eigenvector(clusters=5,weights=karate.es["weight"])
bs5=karate.community_leading_eigenvector(clusters=7,weights=karate.es["weight"])

summary(bs2)
summary(bs3)
summary(bs4)
summary(bs5)

layout=karate.layout_kamada_kawai()
#layout=karate.layout_circle()
#layout=karate.layout_drl()
#layout=karate.layout_fruchterman_reingold

colorlist2=[]
colorlist3=[]
colorlist4=[]
colorlist5=[]

for i in range (0,34):
   colorlist2.append("blue")
   colorlist3.append("blue")
   colorlist4.append("blue")
   colorlist5.append("blue")

for i in range (0,34):
   if i in bs2[0]:
      colorlist2[i]="blue"
   elif i in bs2[1]:
      colorlist2[i]="red"

for i in range (0,34):
   if i in bs3[0]:
      colorlist3[i]="blue"
   elif i in bs3[1]:
      colorlist3[i]="red"
   elif i in bs3[2]:
      colorlist3[i]="green"
      
for i in range (0,34):
   if i in bs4[0]:
      colorlist4[i]="blue"
   elif i in bs4[1]:
      colorlist4[i]="red"
   elif i in bs4[2]:
      colorlist4[i]="green"
   elif i in bs4[3]:
      colorlist4[i]="orange"

for i in range (0,34):
   if i in bs5[0]:
      colorlist5[i]="blue"
   elif i in bs5[1]:
      colorlist5[i]="red"
   elif i in bs5[2]:
      colorlist5[i]="green"
   elif i in bs5[3]:
      colorlist5[i]="orange"
   elif i in bs5[4]:
      colorlist5[i]="pink"

print bs2
print bs3
print bs4
print bs5

plot(karate,layout=layout,vertex_color=colorlist2)
plot(karate,layout=layout,vertex_color=colorlist3)
plot(karate,layout=layout,vertex_color=colorlist4)
plot(karate,layout=layout,vertex_color=colorlist5)
