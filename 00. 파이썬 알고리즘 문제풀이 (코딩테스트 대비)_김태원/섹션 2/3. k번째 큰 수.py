# 조합
# 순열/조합 문제는 아래를 임포트한다음에 라이브러리를 사용하자.

from itertools import *

n, k = map(int, input().split())
num = list(map(int, input().split()))
ans = list()

for a, b, c in combinations(num, 3):
    mSum = a + b + c

    if mSum not in ans:
        ans.append(mSum)

ans.sort(reverse=True)

print(ans[k-1])