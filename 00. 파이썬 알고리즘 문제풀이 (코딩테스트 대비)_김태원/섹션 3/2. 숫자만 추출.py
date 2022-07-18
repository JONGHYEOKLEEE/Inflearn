wordList = list(input())
numList = list()
cnt = 0

for x in wordList:
    if x.isnumeric():
        numList.append(x)

num = int("".join(numList))

for i in range(1, num+1):
    if num % i == 0:
        cnt += 1

print(num, cnt, sep="\n")