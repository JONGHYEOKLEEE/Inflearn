numList = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())

    reverseNumList = numList[a-1:b].copy()
    reverseNumList.reverse()

    numList[a-1:b] = reverseNumList

print(*numList)