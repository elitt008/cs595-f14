#!/usr/bin/python
import feedfilter
import docclass
import feedparser
import randomGram
import unidecode 
#docclass.getwords("this")
myclassifier=docclass.fisherclassifier(docclass.getwords)
myclassifier.setdb('CSblogfeed.db')
#feedfilter.read('CSblogfeed.xml',myclassifier)

#pull in correct answers
file=open('correct.dat','r')
correctf=file.read()
file.close()
correct=correctf.split('\n')

#for line in correct:
#    print line
#del correct[-1]
#print len(correct)
#print type(correct)
#print correctf 
#for item in correctf:
#    print item
f=feedparser.parse('CSblogfeed.xml')
count=0
for entry in f['entries']:
    #train using 50
    if count != 90:
#        print count," ",correct[count]," ",entry['title']
        fulltext='%s\n%s' % (entry['title'],entry['summary'])
        myclassifier.train(fulltext,correct[count])
        count = count + 1
    else: break

cats=myclassifier.categories()
##print type(cats)
#print cats
#myclassifier.setminimum("History",)
#myclassifier.setminimum("Internet",)
#myclassifier.setminimum("AI",)
#myclassifier.setminimum("Hardware",)
#myclassifier.setminimum("Software",)
#myclassifier.setminimum("Education",)


file=open('gram.dat','r')
gramf=file.read()
file.close()
grams=gramf.split('\n')
count=0
for entry in f['entries']:
    #try to classify other 50
    if count >= 90:
        gram=grams[count-50]
    #    for cate in cats:
     #       print cate,myclassifier.fisherprob(gram,cate) 
      #  print count," ",correct[count]," ",entry['title']
#        fulltext='%s\n%s' % (entry['title'],entry['summary'])
#        fulltext=randomGram.randomGram(entry['title']+entry['summary'])
        gram=grams[count-50]
 #       fulltext = fulltext.replace("\"", "")
     #   print "Gram:",gram
#        print "History",myclassifier.cprob(fulltext,"History")
#        print "AI",myclassifier.cprob(fulltext,"AI")
#        print "Hardware",myclassifier.cprob(fulltext,"Hardware")
#        print "Education",myclassifier.cprob(fulltext,"Education")
#        print "Blog",myclassifier.cprob(fulltext,"Blog")
#        print "Internet",myclassifier.cprob(fulltext,"Internet")
#        print "Cyber Security",myclassifier.cprob(fulltext,"Security")
#        print "Software",myclassifier.cprob(fulltext,"Software")
#
#        #print myclassifier.classify(fulltext)
      #  print 'Guess: '+str(myclassifier.classify(gram)) 
        cprob=myclassifier.cprob(gram,correct[count])
        guess=myclassifier.classify(gram)
       # fprob=myclassifier.fisherprob(gram,guess)
        fprob=myclassifier.fisherprob(gram,correct[count])
        #guess=myclassifier.classify(gram)
        #fprob1=myclassifier.fisherprob(gram,guess)
#        print "title: ",entry['title']
#        print "title: ",unidecode.unidecode( entry['title'])
#        print "gram: ",gram
#        print "cprob: ",cprob
#        print "fprob: ",fprob
#        print "guess: ", guess 
#        print "correct: ",correct[count]
#        print "-------------------------------------" 
        #print "\""+unidecode.unidecode(entry['title']),"\",\"",str(gram),"\",\"",round(cprob,3),"\",\"",round(fprob,3),"\",\"", str(guess),"\",\"",str(correct[count])+"\""
        print "\""+unidecode.unidecode(entry['title'])+"\"","\""+str(gram)+"\"","\""+str(round(cprob,3))+"\"","\""+str(round(fprob,3))+"\"","\""+str(guess)+"\"","\""+str(correct[count])+"\""
#        print "-------------------------------------" 
    count = count + 1
