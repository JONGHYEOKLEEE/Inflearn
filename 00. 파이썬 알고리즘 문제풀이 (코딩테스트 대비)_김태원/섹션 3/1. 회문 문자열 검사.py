n = int(input())

for i in range(n):
    reverseWordList = list(input())
    wordList = reverseWordList.copy()
    reverseWordList.reverse()

    word = "".join(wordList)
    reverseWord = "".join(reverseWordList)

    if word.lower() == reverseWord.lower():
        print("#{0} {1}".format(i+1, "YES"))
    else:
        print("#{0} {1}".format(i+1, "NO"))