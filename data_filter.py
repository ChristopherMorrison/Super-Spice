#############################################################
### This file is for parsing the output of the html dump  ###
#############################################################
commons = open("./20k_common_english_words.txt")
commons = commons.read().split()

# read in all the data from filename and run the first
# half of count sort on it to create a dictionary
def readDump(filename):
    # open file
    file = open(filename)
    
    # new dictionary
    wordcount = {}

    # tracking important phrases requires this
    phrase = ""

    # for every word in file
    for word in file.read().split():
        # next word is capital
        if word[0].isupper():
            # add this word to the phrase
            if phrase == "":
                phrase += word
            else:
                phrase += " " + word

        # next word is lowercase
        else:
            # if phrase is not ""
            if not phrase == "":
                # add the phrase to the dictionary and reset it
                if not phrase in wordcount:
                    wordcount[phrase] = 0
                wordcount[phrase] += 1
                phrase = ""

            # add the word to the phrase
            if not word in wordcount:
                wordcount[word] = 0
            wordcount[word] += 1

    # return the dictionary
    return wordcount

# remove words from a list if filter(word) is true
def removeByFilter(wordlist, filter_function):
    # make new wordlist
    newwordlist = {}

    #for word in wordlist
    for word in wordlist:
        # if not filter(word)
        if not filter_function(word):
            # newlist.append word
            newwordlist[word] = wordlist[word]
    
    #return new list
    return newwordlist

# extract words from a list if filter(word) is true
def extractByFilter(wordlist, filter_function):
    # make new wordlist
    newwordlist = {}

    #for word in wordlist
    for word in wordlist:
        # if filter(word)
        if filter_function(word):
            # newlist.append word
            newwordlist[word] = wordlist[word]
    
    #return new list
    return newwordlist

#return true if word is one of the 100 most common words in the english language
def is_common_word(word):
    #if word in commons
    return word in commons

def word_is(compare_word):
    def fn(wrd):
        return wrd == compare_word
    return fn