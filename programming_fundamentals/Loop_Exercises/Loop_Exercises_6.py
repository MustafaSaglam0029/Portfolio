def getmiddle(word):
    lenght = len(word)
    middle = lenght // 2
    if lenght % 2 == 1:
        return word[middle]
    else:
        return word[middle-1:middle+1]
print(getmiddle("test"))
print(getmiddle("testing"))
print(getmiddle("Mustafas"))

