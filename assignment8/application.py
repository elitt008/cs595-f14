#!/usr/bin/python 
import movies
import pickle

pkl_file1 = open('data1.pkl','rb')
pkl_file2 = open('data2.pkl','rb')

movielist = pickle.load(pkl_file1)
userlist = pickle.load(pkl_file2)

pkl_file1.close()
pkl_file2.close()

#highestavg = []
#movies.findHighestAvgRating(movielist,highestavg,4,5)
#print "The highest average ratings were:"
#for rating in highestavg:
#   print rating.avgrating, rating.title, rating.numratings
#
#mostratings = []
#movies.findMostRatings(movielist,mostratings,5)
#print "The movies with the most ratings were:"
#for rating in mostratings:
#   print rating.numratings, rating.avgrating, rating.title
#
#womenAvg = []
#movies.womenHighestAvg(userlist, movielist, womenAvg,5, 5)
#for movie in womenAvg:
#   print movie.slot3, movie.title, movie.slot1, movie.numratings 
#
#menAvg = []
#movies.menHighestAvg(userlist, movielist, menAvg,5, 5)
#for movie in menAvg:
#   print movie.slot3, movie.title, movie.slot1, movie.numratings, movie.avgrating 
#
#topraters = []
#movies.topRaters(userlist, topraters,5)
#for user in topraters:
#   print len(user.ratings), user.i 

womenAvgov40 = []
movies.womenHighestAvgover40(userlist, movielist, womenAvgov40,5, 5)
for movie in womenAvgov40:
   print movie.slot3, movie.title, movie.slot1, movie.numratings 

womenAvgun40 = []
movies.womenHighestAvgunder40(userlist, movielist, womenAvgun40,5, 5)
for movie in womenAvgun40:
   print movie.slot3, movie.title, movie.slot1, movie.numratings

menAvgov40 = []
movies.menHighestAvgover40(userlist, movielist, menAvgov40,5, 5)
for movie in menAvgov40:
   print movie.slot3, movie.title, movie.slot1, movie.numratings

menAvgun40 = []
movies.menHighestAvgunder40(userlist, movielist, menAvgun40,5, 5)
for movie in menAvgun40:
   print movie.slot3, movie.title, movie.slot1, movie.numratings
 
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
