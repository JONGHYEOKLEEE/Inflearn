n, m = map(int, input().split())

nPoly = [x for x in range(1, n+1)]
mPoly = [x for x in range(1, m+1)]
sumList = [0 for _ in range((nPoly[0]+mPoly[0])-1, (nPoly[-1]+mPoly[-1])+1)]

for x in nPoly:
    for v in mPoly:
        sumList[(x+v)-1] += 1

ans = list(filter(lambda x: sumList[x] == max(sumList), range(len(sumList))))

for i in range(len(ans)):
    print(ans[i]+1, end=" ")