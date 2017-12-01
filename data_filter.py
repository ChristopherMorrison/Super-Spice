#############################################################
### This file is for parsing the output of the html dump  ###
#############################################################
commons = open("./20k_common_english_words.txt")
commons = commons.read().split()

# quick unique word filter
def Filter_File(filename, word_count = 10):
    # read in words
    word_list = readDump(filename)

    # filter
    word_list = removeByFilter(word_list, is_common_word)
    word_list = removeByFilter(word_list, is_url)
    word_list = removeByFilter(word_list, is_number)
    word_list = removeByOccuranceMin(word_list,3)
    word_list = extractByFilter(word_list, is_title)
    word_list = extractTopN(word_list, word_count)
    # return
    return word_list

# read data
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

# Filter Types
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
def removeByOccuranceMin(wordlist, occurance_min):
    # make new wordlist
    newwordlist = {}

    #for word in wordlist
    for word in wordlist:
        # if word occurs >= occurance_min times
        if wordlist[word] > occurance_min:
            # newlist.append word
            newwordlist[word] = wordlist[word]
    
    #return new list
    return newwordlist
def extractTopN(wordlist, count):
    newwordlist = {}

    # find the top (count) words in the wordlist and return
    for _ in range(count):
        max_word = ''
        max_value = 0
        for word in wordlist:
            if wordlist[word] > max_value:
                max_word = word
                max_value = wordlist[word]
        newwordlist[max_word] = wordlist.pop(max_word)
        

    return newwordlist

# Filter Functions
def is_common_word(word):
    #if word in commons
    return word.lower() in commons
def word_is(compare_word):
    def fn(wrd):
        return wrd == compare_word
    return fn
def is_url(word):
    return 'https://' in word
def is_number(word):
    return word.isnumeric()
def is_title(word):
    return word.istitle()

# testing area
#x = Filter_File('./article.txt')
#x = extractTopN(x, 10)
#print(x)