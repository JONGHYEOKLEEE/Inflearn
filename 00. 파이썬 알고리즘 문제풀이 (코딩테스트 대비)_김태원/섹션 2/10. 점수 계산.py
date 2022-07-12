n = int(input())
score = list(map(int, input().split()))
ans = 0
cnt = 0

for x in score:
    if x == 1:
        cnt += 1
        ans += cnt
    else:
        cnt = 0

print(ans)