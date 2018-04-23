#!/usr/local/anaconda/bin/python
######################################################################
# YOUR NAME GOES HERE
# YOUR DISCUSSION SECTION (e.g., "A09") GOES HERE
######################################################################

# I certify that the entirety of this file contains only my own
# work. I also certify that I have not shared the contents of this
# file with anyone in any form.

######################################################################
# Replace "hawkid" in the singleton tuple in the function below with
# your own hawkid USING LOWER CASE CHARACTERS ONLY
######################################################################
def hawkid():
    return(("dstutz"))

######################################################################
# f is the opened file then in 'newtext' line.strip removes blank lines in the readlines version of f and then splits the line into a string.
# then text is the comprehension part of the function where it identifies all x in newtext but not if the line is in all uppercase.
def getBook(file):
    f = open(file)
    newtext = [line.strip() for line in f.readlines() if line.split()]
    return(' '.join([x for x in newtext if not x.isupper()]))

######################################################################
# a is the text from getBook
def cleanup(text):
    a = text
    clean = (('(',''), (')',''), (',',''), (':',''), (';',''), ('-', ''), ("'", ''), ('"', ''), ('!', '.'), ('?', '.'))
    for line in clean: #clean is the characters that are being replaced or removed
        if(line[0] in a):
            a = a.replace(line[0],line[1]) #this if statement finds that if the character is equivilent to line[0] then replace it with line[1]
    return(a)

######################################################################
# this function extracts the words from cleanup text in a string
def extractWords(text):
    text = cleanup(text) 
    text = str(text.lower()) #converts text into a string
    nlist = text.split(' ') #splits the string with commas
    nlist.sort() #sorts the string alphabetically
    return(nlist)

######################################################################
# extracts a list of sentences from the designated text
def extractSentences(text):
    text = cleanup(text) 
    return(text.split('.')) #splits the cleaned up sentences with periods

######################################################################
# this function counts the number of syllables in words where a vowel follows a consonant
def countSyllables(word):
    newWord = word
    if (newWord[-1] == "e" or newWord[-1] == "s"): #this if statement removes the trailing s or e in word
        newWord = newWord[0:-1]
    newWord = list(newWord)
    seq = 'aeiouy'
    count = 0
    i = 1
    for x in range(len(newWord)): #this nested for loop is the main piece of this function where it identifies whether or not a vowel is present and if it is followed by a consonant.
        for y in range(len(seq)):
            if newWord[x] == seq[y] and newWord[x-1] not in seq: 
                       count = count + 1
    if count == 0: #accounts for single letter words such as "a"
        count = 1
    return(count)

######################################################################
# This function uses extractSetntences and extractWords to get the ars
def ars(text):
    sList = extractSentences(text)
    count = 0
    for sentence in sList: 
        count = count + len(sentence.split())
    wps = count / len(sList) #number of words/number of sentences
    wordList = extractWords(text)
    counter = 0
    for word in wList:
        counter = counter + len(word) 
    cpw = counter / len(wList) #number of characters/number of words
    return( 4.71*cpw + 0.5*wps - 21.43 )
   

######################################################################
# This function uses extractSentences and extractWords as well as countSyllables to find the fki
def fki(text):
    sList = extractSentences(text)
    count = 0
    for sentence in sList:
        count = count + len(sentence.split())
    wps = count / len(sList) #same as ars
    wList = extractWords(text)
    counter = 0
    for word in wList:
        counter = counter + countSyllables(word)
    spw = counter / len(wList) #uses the number of syllables in counter and gets the number of syllables per the number of words.
    return( 0.39*wps + 11.8*spw - 15.59 )
    

######################################################################
# This function uses both extractSentences and extractWords but sets a limit to per 100 words and sentences
def cli(text):
    sList = extractSentences(text)
    wList = extractWords(text)
    count = 0
    for sentence in sList:
        count = count + len(sentence.split())
    sphw = (len(sList)/(count/100)) #divides the average number of sentences per 100 words 
    counter = 0
    for word in wList:
        counter = counter + len(word)
    cphw = counter / (len(wList)/100) #divides the average number of characters per 100 words
    return(0.0588*cphw-0.296*sphw-15.8)
     
    

######################################################################
# Reads in a book from a file and evaluates its readability. Returns
# None.
def evalBook(file='wind.txt'):
    text = cleanup(getBook(file))
    print("Evaluating {}:".format(file.upper()))
    print("  {:5.2f} Automated Readability Score".format(ars(text)))
    print("  {:5.2f} Flesch-Kincaid Index".format(fki(text)))
    print("  {:5.2f} Coleman-Liau Index".format(cli(text)))
