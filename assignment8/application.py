#!/usr/bin/python 
import movies
import pickle

pkl_file1 = open('data1.pkl','rb')
pkl_file2 = open('data2.pkl','rb')

movielist = pickle.load(pkl_file1)
userlist = pickle.load(pkl_file2)

highestavg = []
movies.findHighestAvgRating(movielist,highestavg,10)

print "The highest average ratings were:"
for rating in highestavg:
   print rating.avgrating, rating.title, rating.numratings

mostratings = []
movies.findMostRatings(movielist,mostratings,10)
print "The movies with the most ratings were:"
for rating in mostratings:
   print rating.numratings, rating.avgrating, rating.title

pkl_file1.close()
pkl_file2.close()

#################################         
#print out the list of movies
#count=0  
#for movie in movielist:
#   count = count+ 1
#   movie.avgrating = movie.calculateavg(userlist)
#   print count, movie.numratings, movie.sumratings, movie.avgrating 

#print out the list of users
#count=0  
#for user in userlist:
#   count = count+ 1
#   print count, user.i, user.age, user.gender, user.occupation, user.zipcode
