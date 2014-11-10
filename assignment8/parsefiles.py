#!/usr/bin/python
import pickle
import movies
################################
#start of program
###############################

userlist=[]
print "Parsing u.data..."
movies.parseData(userlist)

print "Parsing u.user..."
movies.parseUser(userlist)

movielist=[]
print "Parsing u.item..."
movies.parseItem(movielist)

print "Calculating averages..."
for movie in movielist:
   movie.avgrating = movie.calculateavg(userlist)
#movielist=[]     
#for i in range(10):
#   movielist.append(Movie(1,2,3,4,5,6))
#count = 50 
#for movie in movielist:
#   movie.avgrating = count
#   print movie.avgrating
#   count = count + 5

print "Persisting the movielist and userlist..."
output1 = open('data1.pkl' , 'wb')
output2 = open('data2.pkl' , 'wb')
pickle.dump(movielist,output1,-1)
pickle.dump(userlist,output2,-1)
output1.close()
output2.close()
