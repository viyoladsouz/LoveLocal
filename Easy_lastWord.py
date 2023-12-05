def lastWord(sentence):
    words=sentence.split(" ")     #split the string
    return len(words[-1])    #return the length of last word
result=lastWord("Getting into LoveLocal")
print(result)
