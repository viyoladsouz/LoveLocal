def lastWord(sentence):
    words=sentence.split(" ")
    return len(words[-1])
result=lastWord("Getting into LoveLocal")
print(result)