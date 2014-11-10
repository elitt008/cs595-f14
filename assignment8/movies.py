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
      self.listratings = []
      self.avgrating = 0.0
    
   def calculateavg(self, userlist):
      for user in userlist:
         for movie in user.ratings:
            if self.id in movie:
               self.numratings = self.numratings + 1
               self.listratings.append(int(movie[self.id])+0.0)
               self.sumratings = self.sumratings + int(movie[self.id]) + 0.0
               break
      return round((self.sumratings / self.numratings),2)
   def average(self,rating):
      self.avgrating = round(((self.sumratings + rating)/ self.numratings),2)
      return self.avgrating
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

def ordermovielist(movielist):
   count1 = 0
   for movie1 in movielist:
      count2 = 0
      for movie2 in movielist:
         if movie2.avgrating > movie1.avgrating:
            movielist[count1] = movie2
            movielist[count2] = movie1
         count2 = count2 + 1
      count1 = count1 + 1
            
################################

def findHighestAvgRating(movielist,highestmovies,cap):
   for movie in movielist:
      if movie.numratings > 4: 
         if len(highestmovies) < cap:
            highestmovies.append(movie)
            ordermovielist(highestmovies)
         else:
            count=0
            for mov in highestmovies:
               if movie.avgrating > mov.avgrating:
                  highestmovies.insert(count,movie)
                  del highestmovies[-1]
                  break
               count = count + 1
      
################################

def findMostRatings(movielist,mostratings,cap):
   for movie in movielist:
       
      if len(mostratings) < cap:
         mostratings.append(movie)
         ordermovielist(mostratings)
      else:
         count=0
         for mov in mostratings:
            if movie.numratings > mov.numratings:
               mostratings.insert(count,movie)
               del mostratings[-1]
               break
            count=count + 1

