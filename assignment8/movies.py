#!/usr/bin/python
class User:
   def __init__(self,uid,movie,rating):
      self.i = uid
      self.ratings = []
      self.age = ""
      self.gender = ""
      self.occupation = ""
      self.zipcode = ""
      self.addrating(movie,rating)
   def addrating(self,movie, rating):
      self.ratings.append({movie : rating})
################################

class Movie:
   def __init__(self, mid, title, rd, videord, imdb, genre ):
      self.id = mid
      self.title = title
      self.releasedate = rd
      self.vidreleasedate = videord
      self.imdburl = imdb  
      self.genre = genre

      self.numratings = 0
      self.sumratings = 0.0
      self.avgrating = 0.0

      self.slot1 = 0
      self.slot2 = 0.0
      self.slot3 = 0.0

   def calculateavg(self, userlist):
      self.slot1 = 0
      self.slot2 = 0.0
      self.slot3 = 0.0
      for user in userlist:
         for movie in user.ratings:
            if self.id in movie:
               self.slot1 = self.slot1 + 1
               #self.listratings.append(int(movie[self.id])+0.0)
               self.slot2 = self.slot2 + int(movie[self.id]) + 0.0
               break
      if self.slot1 > 0:
         return round((self.slot2 / self.slot1),2)
      else:
        return 0.00

################################

def parseItem(movielist):
   fd = open('u.item', 'r')
   while True:
      line = fd.readline()
      if line == '': 
         break
      parsed=line.rsplit('|')
      genre=''.join(map(str,parsed[5:]))
      movielist.append(Movie(parsed[0],parsed[1],parsed[2],
                       parsed[3],parsed[4],genre))
   fd.close() 

################################

def parseData(userlist):
   fd = open('u.data', 'r')
   while True:
      line = fd.readline()
      if line == '': 
         break
  
      parsed=line.rsplit()
      notexist=True
      for user in userlist:
         if user.i == parsed[0]:
            user.addrating(parsed[1],parsed[2])
            notexist=False
      if notexist:
         userlist.append(User(parsed[0],parsed[1],parsed[2]))
   fd.close() 

################################

def parseUser(userlist):
   fd = open('u.user','r')
   while True:
      line = fd.readline()
      if line == '': 
         break
      parsed = line.rsplit('|')
      for user in userlist:
         if user.i == parsed[0]:
            user.age = parsed[1]
            user.gender = parsed[2]
            user.occupation = parsed[3]
            user.zipcode = parsed[4]
            break
   fd.close()

################################
# by slot 3 , slot1, average or number of ratings
#def ordermovielist(movielist,selector):
#   count1 = 0
#   for movie1 in movielist:
#      count2 = 0
#      for movie2 in movielist:
#         if (selector == 0 and movie2.avgrating > movie1.avgrating) or \
#            (selector == 1 and movie2.numratings > movie1.numratings) or \
#            (selector == 2 and movie2.slot3 > movie1.slot3) or \
#            (selector == 3 and movie2.slot1 > movie2.slot1):
#             movielist.insert(count1,movie2)
#             movielist.insert(count2,movie1)
#             del movielist[count1+1]
#             del movielist[count2+1]
#         #   movielist[count1] = movie2
#         #   movielist[count2] = movie1
#         count2 = count2 + 1
#      count1 = count1 + 1

################################

#def orderuserlist(userlist):
#   count1 = 0
#   for user1 in userlist:
#      count2 = 0
#      for user2 in userlist:
#         if len(user2.ratings) > len(user1.ratings):
#            userlist[count1] = user2
#            userlist[count2] = user1
#         count2 = count2 + 1
#      count1 = count1 + 1

################################1

def findHighestAvgRating(movielist,highestmovies,min,cap):
   for movie in movielist:
      if movie.numratings > min: 
         if len(highestmovies) < cap:
            highestmovies.append(movie)
            #ordermovielist(highestmovies,0)
         else:
            count=0
            for mov in highestmovies:
               if movie.avgrating > mov.avgrating:
                  highestmovies.insert(count,movie)
                  del highestmovies[-1]
                  break
               count = count + 1

################################2

def findMostRatings(movielist,mostratings,cap):
   for movie in movielist:
      if len(mostratings) < cap:
         mostratings.append(movie)
         #ordermovielist(mostratings,1)
      else:
         count=0
         for mov in mostratings:
            if movie.numratings > mov.numratings:
               mostratings.insert(count,movie)
               del mostratings[-1]
               break
            count=count + 1

################################3

def womenHighestAvg(userlist,movielist,arrangedlist,min,cap):
    print "Finding all women..."
    genderlist=[]
    for user in userlist:
        if user.gender == "F":
            genderlist.append(user)
    print "Calculating women average..."
    for movie in movielist:
        average = movie.calculateavg(genderlist)
        movie.slot3 = average
        if movie.slot1 > min:
            if len(arrangedlist) < cap:
                arrangedlist.append(movie)
                #ordermovielist(arrangedlist,2)
            else:
                count=0
                for mov in arrangedlist:
                    if movie.slot3 > mov.slot3:
                        arrangedlist.insert(count,movie)
                        del arrangedlist[-1]
                        break
                    count = count + 1

################################4

def menHighestAvg(userlist,movielist,arrangedlist,min,cap):
    print "Finding all men..."
    genderlist=[]
    for user in userlist:
        if user.gender == "M":
            genderlist.append(user)
    print "Calculating men average..."
    for movie in movielist:
        average = movie.calculateavg(genderlist)
        movie.slot3 = average
        if movie.slot1 > min:
            if len(arrangedlist) < cap:
                arrangedlist.append(movie)
                #ordermovielist(arrangedlist,2)
            else:
                count=0
                for mov in arrangedlist:
                    if movie.slot3 > mov.slot3:
                        arrangedlist.insert(count,movie)
                        del arrangedlist[-1]
                        break
                    count = count + 1

################################5

def compareMovie(movielist,movie1,movie2):
    print "unimplemented function"

################################6

def topRaters(userlist,arrangedlist,cap):
   print "Finding users with the most reviews..."
   for user in userlist:
      if len(arrangedlist) < cap:
         arrangedlist.append(user)
         #orderuserlist(arrangedlist)
      else:
         count=0
         for person in arrangedlist:
            if len(user.ratings) > len(person.ratings):
               arrangedlist.insert(count,user)
               del arrangedlist[-1]
               break
            count=count + 1

################################9

def womenHighestAvgover40(userlist,movielist,arrangedlist,min,cap):
    print "Finding all women over 40..."
    genderlist=[]
    for user in userlist:
        if user.gender == "F" and int(user.age) > 40:
            genderlist.append(user)
    print "Calculating women over 40 average..."
    for movie in movielist:
        average = movie.calculateavg(genderlist)
        movie.slot3 = average
        if movie.slot1 > min:
            if len(arrangedlist) < cap:
                arrangedlist.append(movie)
                #ordermovielist(arrangedlist,2)
            else:
                count=0
                for mov in arrangedlist:
                    if movie.slot3 > mov.slot3:
                        arrangedlist.insert(count,movie)
                        del arrangedlist[-1]
                        break
                    count = count + 1


################################10
def menHighestAvgover40(userlist,movielist,arrangedlist,min,cap):
    print "Finding all men over 40..."
    genderlist=[]
    for user in userlist:
        if user.gender == "M" and int(user.age) > 40:
            genderlist.append(user)
    print "Calculating men over 40 average..."
    for movie in movielist:
        average = movie.calculateavg(genderlist)
        movie.slot3 = average
        if movie.slot1 > min:
            if len(arrangedlist) < cap:
                arrangedlist.append(movie)
                #ordermovielist(arrangedlist,2)
            else:
                count=0
                for mov in arrangedlist:
                    if movie.slot3 > mov.slot3:
                        arrangedlist.insert(count,movie)
                        del arrangedlist[-1]
                        break
                    count = count + 1
##################################
def womenHighestAvgunder40(userlist,movielist,arrangedlist,min,cap):
    print "Finding all women under 40..."
    genderlist=[]
    for user in userlist:
        if user.gender == "F" and int(user.age) < 40: 
            genderlist.append(user)
    print "Calculating women under 40 average..."
    for movie in movielist:
        average = movie.calculateavg(genderlist)
        movie.slot3 = average
        if movie.slot1 > min:
            if len(arrangedlist) < cap:
                arrangedlist.append(movie)
                #ordermovielist(arrangedlist,2)
            else:
                count=0
                for mov in arrangedlist:
                    if movie.slot3 > mov.slot3:
                        arrangedlist.insert(count,movie)
                        del arrangedlist[-1]
                        break
                    count = count + 1 
################################10
def menHighestAvgunder40(userlist,movielist,arrangedlist,min,cap):
    print "Finding all men under 40..."
    genderlist=[]
    for user in userlist:
        if user.gender == "M" and int(user.age) < 40:
            genderlist.append(user)
    print "Calculating men under 40 average..."
    for movie in movielist:
        average = movie.calculateavg(genderlist)
        movie.slot3 = average
        if movie.slot1 > min:
            if len(arrangedlist) < cap:
                arrangedlist.append(movie)
                #ordermovielist(arrangedlist,2)
            else:
                count=0
                for mov in arrangedlist:
                    if movie.slot3 > mov.slot3:
                        arrangedlist.insert(count,movie)
                        del arrangedlist[-1]
                        break
                    count = count + 1
##################################################
#def findnextcorrelationlist(relationlist, previouslist, num,rp,sign)
#    topcorrelations = []
#    for item1 in previouslist:
#        for item2 in relationlist:
#            if item2[1] == item2[2]:
#                templist = []
#                for i in range(0,num - 1):
#                    templist.append(item1[i])
#                templist.append(item2[2])
#                topcorrelations.append(templist)
#    removeDuplicates(topcorrelations)
#    correlateItems(topcorrelations,prefs,level,rp,sign)
#    return topcorrelations
###################################################
#def removeDuplicates(correlationlist)
#    count = 0 
#    removeindex = []
#    for item in correlationlist:
#        if len(item) != len(set(item)):
#            removeindex.append(count)
#        count = count + 1 
#
#    count = 0 
#    for integer in removeindex:
#        del correlationlist[integer - count]
#        count = count + 1
####################################################
#def correlateItems(correlationlist,prefs,level,rp,sign)
#    count = 0
#    removeindex = []
#    for item in correlationlist:
#        pearsonstuff(level,removeindex,0,rp,sign)
#        count = count + 1
#
#    count = 0
#    for integer in removeindex:
#        del correlationlist[integer - count]
#        count = count + 1
######################################################
#def pearsonstuff(num,removeindex,count,rp,sign)
#    pearson = recommendations.sim_pearson(prefs,item[0],item[3])
#    count = count + 1
#    if (sign * pearson) < (sign * rp):
#        removeindex.append(count)
#    elif((num-2) == count):
##        pearsonstuff(num,removeindex,count,rp,sign)
#    
#
