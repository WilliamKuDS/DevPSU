translateInput = input("What would you like me to translate into Pig Latin?") + " "
translatedSentence = ""
currentWord = ""
vowelList = ["a","e","i","o","u","y"]

for x in range(len(translateInput)):
    if translateInput[x] == ' ':
        for y in range(len(currentWord)):
            if currentWord[y] in vowelList:
                currentWord = currentWord[y:] + currentWord[:y] + "yay "
                translatedSentence += currentWord
                currentWord = ""
                break
    else:
        currentWord += translateInput[x]
print (translatedSentence)