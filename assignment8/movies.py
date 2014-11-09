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
   def calculateavg(self, userlist):
      for user in userlist:
         for movie in user.ratings:
            if self.id in movie:
               self.numratings = self.numratings + 1
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
#start of program
###############################

userlist=[]
parseData(userlist)
parseUser(userlist)
movielist=[]

parseItem(movielist)

#calculate avg 
for movie in movielist:
   movie.avgrating = movie.calculateavg(userlist)

      
      

#count=0  
#for movie in movielist:
#   count = count+ 1
#   movie.avgrating = movie.calculateavg(userlist)
#   print count, movie.numratings, movie.sumratings, movie.avgrating 
#count=0  
#for user in userlist:
#   count = count+ 1
#   print count, user.i, user.age, user.gender, user.occupation, user.zipcode
