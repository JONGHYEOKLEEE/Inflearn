n = int(input())
num = list(map(str, input().split()))
digitSum = list()

def digit_sum(x):
    for v in x:
        total = 0

        for i in range(len(v)):
            total += int(v[i])
        
        digitSum.append(total)

    ans = list(filter(lambda x: digitSum[x] == max(digitSum), range(len(digitSum))))

    for idx in ans:
        print(num[idx], end=" ")

digit_sum(num)