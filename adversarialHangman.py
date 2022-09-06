import re

with open(r"google-10000-english-usa-no-swears.txt","r+") as f:
    allWords = f.read().split('\n')

wordLength = 0
while (wordLength < 1 or wordLength > len(max(allWords, key = len))):
    wordLength = int(input("What word length do you want to play with? (1-18): "))

possibleWords = [i for i in allWords if len(i) == wordLength]
playerPattern = "_" * wordLength
guessedLetters = set('_')
guessedLetter = '_'

while True:
    searchSpace = dict()
    print("-----------------------------------------------------------")
    print("\nGuessed Letters:", guessedLetters)
    while guessedLetter in guessedLetters:
        guessedLetter = input(playerPattern + "\nGuess: ")
        if guessedLetter in guessedLetters:
            print("You already guessed this letter.")
    guessedLetters.add(guessedLetter)

    for word in possibleWords:
        if playerPattern == "_" * wordLength:
            pattern = "_" * wordLength
        else:
            pattern = playerPattern
        res = [i for i in range(len(word)) if word.startswith(guessedLetter, i)]
        for i in res:
            pattern = pattern[:i] + guessedLetter + pattern[i+1:]
        if pattern not in searchSpace:
            searchSpace[pattern] = []
        
        searchSpace[pattern].append(word)

    temp = -1
    for patterns in searchSpace:
        if len(searchSpace[patterns]) > temp:
            temp = len(searchSpace[patterns])
            playerPattern = patterns

    possibleWords = searchSpace[playerPattern]

    if "_" not in playerPattern:
        print("-----------------------------------------------------------")
        print("\nYou win! The word was " + "\"" + possibleWords[0] + "\"" + ".")
        break
