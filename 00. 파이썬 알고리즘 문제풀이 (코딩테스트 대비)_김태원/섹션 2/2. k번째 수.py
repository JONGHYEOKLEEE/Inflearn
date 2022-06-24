t = int(input())
ans = list()

for _ in range(t):
    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    
    # 리스트를 슬라이싱 한 후 바로 sort() 해버리면 안 먹는다.. (ex. num[s-1:e-1].sort())
    # 그래서 나눠서 해야 하고, 슬라이싱 수행해도 원본 리스트는 변하지 않는다.
    numSlice = num[s-1:e]
    numSlice.sort()

    ans.append(numSlice[k-1])

for index, v in enumerate(ans):
    print("#{0} {1}".format(index+1, v))