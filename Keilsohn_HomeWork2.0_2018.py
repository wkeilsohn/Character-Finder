# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:01:09 2018

@author: William Keilsohn
"""

# Import the nltk books

from nltk.book import *

# Find all words that end in "ize"

seeNo = "Nothing to see here." #As I use this multiple times, I am drying out my code by defining it once. 

def izeFinder(book):
    izeLis = []
    for i in book: #https://stackoverflow.com/questions/33030377/finding-words-ending-in-letters-it-while-negating-all-other-words
        if i.endswith('ize'): #https://stackoverflow.com/questions/37618224/how-to-check-if-a-string-ends-in-a-certain-way
            izeLis.append(i)
        if len(izeLis) == 0:
            izeLis.append(seeNo) #Turns out there are none. Longer explination at the very bottom.
    return izeLis

# Find all words with the leter Z

def zFinder(book):
    zLis = []
    for i in book:
        if 'z' in i: #https://stackoverflow.com/questions/3962846/how-to-display-all-words-that-contain-these-characters
            zLis.append(i)
    return zLis

# Find all words with "pt" in them
    
def ptFinder(book):
    ptLis = []
    for i in book:
        if 'pt' in i: #https://stackoverflow.com/questions/3962846/how-to-display-all-words-that-contain-these-characters
            ptLis.append(i)
    return ptLis

# Find words where only the first letter is capitalized. 

def capFinder(book):
    capLis = []
    for i in book:
        if i[0].isupper(): #https://stackoverflow.com/questions/7353968/checking-if-first-letter-of-string-is-in-uppercase
            capLis.append(i)
    return capLis

# I  want a helper function and a few helful lists to count some output

def wordCounter(book):
    wordLis = []
    if izeFinder(book)[0] == seeNo: #Accounts for not every book having all text in question. 
        wordLis.append(str(0))
    else:
        wordLis.append(str(len(izeFinder(book))))
    wordLis.append(str(len(zFinder(book))))
    wordLis.append(str(len(ptFinder(book))))
    wordLis.append(str(len(capFinder(book)))) #Probably safe to assume something is captilaized in every book. 
    return wordLis

keyWordLis = ["end in 'ize'.", " contain 'z'.", "contain 'pt'.", "start with a capital letter."] #Fills in the file with all possible word combos
keyFunLis = [izeFinder, zFinder, ptFinder, capFinder] #Fills in the fill with all possible searched for words.


# Write a file with the desired output


def fileWriter(book):
    bookFile = open("bookfile.txt", "w")
    bookFile.write("Below in an analysis of the text: ")
    bookFile.write(book.name) #You can apparently just call a book by its cover.
    bookFile.write("\n")
    bookFile.write("\n") # Makes the spacing look nicer.
    for i in range(0, 4):
        bookFile.write("There are a total of ")
        bookFile.write(wordCounter(book)[i]) #There may not actually be any "ize" in MP & The Holy Grail
        bookFile.write(" word(s) that ")
        bookFile.write(keyWordLis[i])
        bookFile.write("\n")
        bookFile.write("They are:\n")
        bookFile.write(str(keyFunLis[i](book)))
        bookFile.write("\n")
        bookFile.write("\n") #Looks nicer with some extra space. 
    bookFile.close()
        
  
fileWriter(text6) # Answers all questions. 

'''
---To check that there are no words with 'ize' first print out all of text6.
testFile = open("testfile.txt", "w")
for i in text6:
    testFile.write(str(i))
testFile.close()
---Then just use Ctrl + F to check that there are no 'ize' words.
'''