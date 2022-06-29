n = int(input())
num = [0] * (n+1)
ans = 0

for i in range(2, n+1):
    if num[i] == 0:
        ans += 1

        for j in range(i, n+1, i):
            num[j] = 1

print(ans)