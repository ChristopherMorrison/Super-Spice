#############################################################
### This file is for parsing the output of the html dump  ###
#############################################################



# read in all the data from filename and run the first
# half of count sort on it to create a dictionary
def readDump(filename):
    return
    # open file
    file = open(filename, "r")
    print(file)
    print("test")
    
    # new dictionary
    wordcount = {}
    wordcount

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
                wordcount[phrase] += 1
                phrase = ""

            # add the word to the phrase
            wordcount[word] += 1

    # return the dictionary
    return wordcount


# remove words from a list if filter(word) is true
def removeByFilter(wordlist, filter):
    # make new wordlist
    #for word in wordlist
        # if not filter(word)
            # newlist.append word
    #return new list
    return

# extract words from a list if filter(word) is true
def extractByFilter(wordlist, filter):
    # make new wordlist
    #for word in wordlist
        # if filter(word)
            # newlist.append word
    #return new list
    return


#return true if word is one of the 100 most common words in the english language
def is_common_word(word):
    #if word in commons
    return

