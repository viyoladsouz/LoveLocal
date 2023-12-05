sentence="Getting into LoveLocal"
def lastWord(sentence):
    words=sentence.split(sentence)  #split the string
    return len(words[-1]) #return the length of last word 
result=lastWord()
print(result)
