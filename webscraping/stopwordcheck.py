############################################################################
'''
started with trying to loop through words
then created lists of postive and negative words and compared against bag of words
removed stop words, punctuations and applied lower case, did some basic word count analysis
added in logging, removed all print statements
stopwords and bagofwords are being read from text files
added basic info about files being read

yet to do
- need to optimize the code for looping through and comparing words
- be able to read multiple files from a given folder, and ignore non text files
- add in file reading for positive and negative words
- add the testing modules
- add timer - time taken to reach each file, time taken to analyze each file
- add try and catch and exception handling
- in the basic file info section, should be able to read and print the name of the file
- in the File analysis section, add the top 5 words and their occurances (frequency) per document
- integrate word cloud
-given a word what other words occur with it (word associations table)

'''

################################for logging copy below code####################
import logging
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="D:\\Python Programs\\webscraping\\mylog.txt",
                    level = logging.INFO,
                    format = LOG_FORMAT,
                    filemode="w"
                   )

logger = logging.getLogger()
#filemode = "w" menas it will overwrite the previous logs, if you want it to append to previous logs, make ""
#logger.info("this is an info message")
#logger.debug("this is a debug message")
#logger.warning("this is a warning message")
#logger.critical("this is a critical message")
##################### for logging copy above code block ############################

############################# This is for importing files#################
# write code to read stop words from a file, the stop word files are downloaded into webscraping folder from https://bitbucket.org/kganes2/text-mining-resources/downloads/
# write code to get a list of stop words from this website and get it into a list "stopwords" use this for testing https://bitbucket.org/kganes2/text-mining-resources/downloads/
stopwordspath="D:\Python Programs\webscraping\stopwords"
punctuationpath=""
poswordspath=""
negwords=""
bagofwardspath="D:\Python Programs\webscraping\mytestfile"
print(bagofwardspath)


#print(swords)
#swords.close()

#print(swords[0])

#################################Below is the code to eextract out stop words, punctuations, positive, negative words ###################
# want to remove stop words, punctuation, from a bag of words and then count the positive and negative words

#stopwords=["a","the","The","is","if","but","about","and","if","but"]
stopwords=open(stopwordspath,"r").read().lower()
#print(stopwords)
logger.info("After reading stopwords file")
punctuation=[",",".","?",":",";","?","{","}","[","]","(",")","|"]
poswords=["good","super","excellent","beautiful","welcomes"]
negwords=["bad","ugly","stupid","bastard","fool"]
#bagofwords= ["My","name","is","ravi","the","a",",","?","good","bad","ugly","beautiful","stupid", "KRISHNA", "ABOUT","about","ALMOST","almost","RAVI"]
bagofwords=open(bagofwardspath,"r").read().split()
logger.info("After reading test file")

################################################# Term Frequency ############################################

############################################################################################################


######################################## FILE INFO #################################
# the file size, file path ,number of characters and number of lines in a file,
logger.info("########### This info about the files being read ###########")

logger.info("########### This info about STOPWORDS its file size is : " + str(stopwords.__len__()) + " kb")
logger.info("########### The file path for STOPWORDS is : " + stopwordspath)
logger.info("########### STOPWORDS file has : " + str(len(stopwords))+" words")
logger.info("########### This info about  MYTEST its file size is : " + str(bagofwords.__len__()) + " kb")
logger.info("########### The file path for MYTEST is : " + bagofwardspath)
logger.info("########### MYTEST file has : " + str(len(bagofwords))+" words")


print(stopwords.__len__())

logger.info("########### This info about sample file which is read ###########")



logger.info("########### This info about the files being read ###########")


#######################################################################################

#print("Starting List of Stop words -->"+str(bagofwords)+"Total number of words: "+str(len(bagofwords)))
logger.info("Starting List of Stop words -->Total number of words: "+str(len(bagofwords)))

#convert all to lower case
print("Before converting to lower case -->" + str(bagofwords[0:100]))
bagofwords = [item.lower() for item in bagofwords] # This is super efficient code !!!!!
print("After converting to lower case -->" + str(bagofwords))
logger.info("After converting to lower case -->")

#remove repeat words ??? this should not be applied for all text analysis , doing this here for learning

# construct n gram, write for 2 and 3 word phrases

#remove stop words
for word in stopwords:
    if word in bagofwords:
        #print("a stop word is found: " + word)
        bagofwords.remove(word)
#print("After removing stop words-->" + str(bagofwords)+"Total number of words: "+str(len(bagofwords)))
logger.info("After removing stop words-->Total number of words: "+str(len(bagofwords)))

for p in punctuation:
    if p in bagofwords:
        #print("a punctuation is found: " + p)
        bagofwords.remove(p)
#print("After removing punctuation-->" + str(bagofwords)+" Total number of words: "+str(len(bagofwords)))
logger.info("After removing punctuation-->Total number of words: "+str(len(bagofwords)))

pword=0
for p in bagofwords :
    if p in poswords:
        pword=1+pword
#print("Positive words-->" + str(pword)+" Total number of words: "+str(len(bagofwords))+" Percentage of Positive words : "+str((pword/len(bagofwords))*100)+"%")
logger.info("Positive words-->" + str(pword)+" Total number of words: "+str(len(bagofwords))+" Percentage of Positive words : "+str((pword/len(bagofwords))*100)+"%")

nword=0
for n in negwords :
    if n in bagofwords:
       nword=nword+1
#print("Negative words-->" + str(nword)+" Total number of words: "+str(len(bagofwords))+" Percentage of Negative words : "+str((nword/len(bagofwords))*100)+"%")
logger.info("Negative words-->" + str(nword)+" Total number of words: "+str(len(bagofwords))+" Percentage of Negative words : "+str((nword/len(bagofwords))*100)+"%")

################################## FILE ANALYSIS #############################################
logger.info("########### This Analysis is about  MYTEST file , its file size is : " + str(bagofwords.__len__()) + " kb")
logger.info("########### The file path for MYTEST is : " + bagofwardspath)
logger.info("########### MYTEST file has : " + str(len(bagofwords))+" words")
logger.info("########### MYTEST file has : " + str(pword)+" positive words")
logger.info("########### MYTEST file has : " + str(nword)+" negative words")

############################################################################################