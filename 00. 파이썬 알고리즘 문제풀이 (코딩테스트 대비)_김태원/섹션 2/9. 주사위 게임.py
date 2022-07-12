n = int(input())
ans = list()

for _ in range(n):
    dice = list(map(int, input().split()))
    maxCount = 0
    maxCountIdx = 0

    for idx, x in enumerate(dice):
        if maxCount < dice.count(x):
            maxCount = dice.count(x)
            maxCountIdx = idx
    
    if maxCount == 3:
        ans.append(10000+dice[maxCountIdx]*1000)
    elif maxCount == 2:
        ans.append(1000+dice[maxCountIdx]*100)
    else:
        ans.append(max(dice)*100)

print(max(ans))