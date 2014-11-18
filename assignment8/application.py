#!/usr/bin/python 
import movies
import pickle
import recommendations

pkl_file1 = open('data1.pkl','rb')
pkl_file2 = open('data2.pkl','rb')

movielist = pickle.load(pkl_file1)
userlist = pickle.load(pkl_file2)

pkl_file1.close()
pkl_file2.close()

##queston 1
count = 0
highestavg = []
movies.findHighestAvgRating(movielist,highestavg,3,5)
print "The highest average ratings were:"
for rating in highestavg:
   count = count + 1;
   print str(count)+".", rating.avgrating, rating.title#, rating.numratings

#question 2
count = 0
mostratings = []
movies.findMostRatings(movielist,mostratings,5)
print "The movies with the most ratings were:"
for rating in mostratings:
   count = count + 1;
   print str(count)+".",rating.numratings, rating.title#, rating.avgrating

#question 3
count = 0
womenAvg = []
movies.womenHighestAvg(userlist, movielist, womenAvg,3, 5)
for movie in womenAvg:
   count = count + 1;
   print str(count)+".",movie.slot3, movie.title#, movie.slot1, movie.numratings 
#
###queston 4
count = 0
menAvg = []
movies.menHighestAvg(userlist, movielist, menAvg, 3, 5)
for movie in menAvg:
   count = count + 1;
   print str(count)+".",movie.slot3, movie.title#, movie.slot1, movie.numratings, movie.avgrating 

#question 6
count = 0
topraters = []
movies.topRaters(userlist, topraters,5)
for user in topraters:
   count = count + 1;
   print str(count)+".", user.i, len(user.ratings)

#question 10
count = 0
womenAvgov40 = []
movies.womenHighestAvgover40(userlist, movielist, womenAvgov40,3, 5)
for movie in womenAvgov40:
   count = count + 1
   print str(count)+".", movie.slot3, movie.title#, movie.slot1, movie.numratings 
#
##question 10
count = 0
womenAvgun40 = []
movies.womenHighestAvgunder40(userlist, movielist, womenAvgun40,3, 5)
for movie in womenAvgun40:
   count = count + 1
   print str(count)+".", movie.slot3, movie.title#, movie.slot1, movie.numratings

#question 9


menAvgov40 = []
count = 0
movies.menHighestAvgover40(userlist, movielist, menAvgov40,3, 5)
for movie in menAvgov40:
   count = count + 1
   print str(count)+".",movie.slot3, movie.title#, movie.slot1, movie.numratings
##
###question 9
menAvgun40 = []
count = 0
movies.menHighestAvgunder40(userlist, movielist, menAvgun40,3, 5)
for movie in menAvgun40:
   count = count + 1
   print str(count)+".",movie.slot3, movie.title#, movie.slot1, movie.numratings

#question 5
#prefs = recommendations.loadMovieLens()
#simItem = recommendations.calculateSimilarItemsTopGun(prefs,5)
##simItem1 = recommendations.calculateSimilarItems(prefs,10)
#count = 1 
#print "The positive correlations are:"
#for item in simItem['Top Gun (1986)']:
#    if item[0] > 0:
#        print str(count)+".",item[0], item[1]
#        count = count + 1
#
#count = 1 
#print "The negative correlations are:"
#for item in simItem['Top Gun (1986)']:
#    if item[0] < 0:
#        print str(count)+".",item[0], item[1]
#        count = count + 1
#####################################################################
#question 7 and 8
##print "Finding Pearson coeffiecient..."
##pearsonlist = []
##for person1 in userlist:
##    for person2 in userlist:
##        if person1.i != person2.i: 
##            pearson = recommendations.sim_pearson(prefs,person1.i,person2.i) 
##            member = [pearson,person1.i,person2.i]
##            pearsonlist.append(member)
##    del userlist[0]
##
##print "Finding top correlations..."
##topcorrelations = []
##for item in pearsonlist:
##    if item[0] >= 1:
##        topcorrelations.append(item)
######################################top3
##print "Finding top 3 correlations..."
##top3correlations = []
##for item1 in topcorrelations:
##    for item2 in topcorrelations:
##        if item2[1] == item1[2]:
##            top3correlations.append([item1[1],item1[2],item2[2]])
##
##print len(top3correlations)
##
##removeindex = []
##print "Removing duplicates from top3correlations..."
##count = 0
##for item in top3correlations:
##    if len(item) != len(set(item)):
##        removeindex.append(count)
##    count = count + 1
##print len(top3correlations)
##
##count = 0;
##for integer in removeindex:
###    print integer
##    del top3correlations[integer - count]
##    count = count + 1 
##print len(top3correlations)
###
##print "Correlating items and checking to each other..."
##count = 0
##removeindex = []
##for item in top3correlations:
##    pearson = recommendations.sim_pearson(prefs,item[0],item[2])
##    if pearson < 1:
##        removeindex.append(count)
##    count = count + 1
##
##count = 0;
##for integer in removeindex:
##    del top3correlations[integer - count]
##    count = count + 1 
##print len(top3correlations)
###
###
######################################top4
#print "Finding top 4 correlations..."
#top4correlations = []
#for item1 in top3correlations:
#    for item2 in topcorrelations:
#        if item2[1] == item1[2]:
#            top4correlations.append([item1[0],item1[1],item1[2],item2[2]])
#print len(top4correlations)
#
#print "Removing duplicates from top4correlations..."
#count = 0
#removeindex = []
#for item in top4correlations:
#    if len(item) != len(set(item)):
#        removeindex.append(count)
#    count = count + 1
#print len(top4correlations)
#
#count = 0;
#for integer in removeindex:
#    del top4correlations[integer - count]
#    count = count + 1 
#print len(top4correlations)
#
#print "Correlating items and checking to each other..."
#count = 0
#removeindex = []
#for item in top4correlations:
#    pearson = recommendations.sim_pearson(prefs,item[0],item[3])
#    if pearson < 1:
#        #del top4correlations[count]
#        removeindex.append(count)
#    else:
#        pearson = recommendations.sim_pearson(prefs,item[1],item[3])
#        if pearson < 1:
#            removeindex.append(count)
#            #del top4correlations[count] 
#    count = count + 1
#
#print len(top4correlations)
#
#count = 0;
#for integer in removeindex:
#    del top4correlations[integer - count]
#    count = count + 1 
#print len(top4correlations)
#####################################top5
#
#print "Finding top 5 correlations..."
#top5correlations = []
#for item1 in top4correlations:
#    for item2 in topcorrelations:
#        if item2[1] == item1[3]:
#            top5correlations.append([item1[0],item1[1],item1[2],item1[3],item2[2]])
#print len(top5correlations)
#
#print "Removing duplicates from top5correlations..."
#count = 0
#removeindex = []
#for item in top5correlations:
#    if len(item) != len(set(item)):
#        removeindex.append(count)
#    count = count + 1
#print len(top5correlations)
#
#count = 0;
#for integer in removeindex:
#    del top5correlations[integer - count]
#    count = count + 1 
#print len(top5correlations)
#
#
#print "Correlating items and checking to each other..."
#count = 0
#removeindex = []
#for item in top5correlations:
#    pearson = recommendations.sim_pearson(prefs,item[0],item[4])
#    if pearson < .7:
#        removeindex.append(count)
#    else:
#        pearson = recommendations.sim_pearson(prefs,item[1],item[4])
#        if pearson < .7:
#            removeindex.append(count)
#        else:
#            pearson = recommendations.sim_pearson(prefs,item[2],item[4])
#            if pearson < .7:
#                removeindex.append(count)
#    count = count + 1
#
#count = 0;
#for integer in removeindex:
#    del top5correlations[integer - count]
#    count = count + 1 
#print len(top5correlations)
#
#simatrix = []
#for item in top5correlations:
#    itematrix = []
#    for id1 in item:
#        for id2 in item:
#            if id1
 
##print "Finding highest and lowest coeffiecient..."
#templisthigh = [[-2,0,0]]*5
#templistlow = [[2,0,0]]*5
#for member in pearsonlist:
#    count = 0
#    for element in templisthigh:
#        if member[0] > element[0]:
#            templisthigh.insert(count,member)
#            del templisthigh[-1]
#            break
#        count = count + 1 
#    count = 0
#    for element in templistlow:
#        if member[0] < element[0]:
#            templistlow.insert(count,member)
#            del templistlow[-1]
#            break
#        count = count + 1 
#
#for member in templisthigh:
#    print member[0],member[1],member[2]
#
#for member in templistlow:
#    print member[0],member[1],member[2]

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
