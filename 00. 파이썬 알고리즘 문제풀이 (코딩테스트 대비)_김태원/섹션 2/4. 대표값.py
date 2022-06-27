n = int(input())
student = list(map(int, input().split()))

# scoreAvg = round(sum(student) / n)
# python 에서 round 함수는 round_half_even 방식임.
# 따라서 round_half_up을 하려면 아래와 같이해야함.
scoreAvg = int((sum(student) / n) + 0.5)
diff = abs(scoreAvg-student[0])
idx = 0

for index, x in enumerate(student):
    if diff > abs(scoreAvg-x):
        diff = abs(scoreAvg-x)
        idx = index
    elif diff == abs(scoreAvg-x):
        if student[index] > student[idx]:
            idx = index
        elif student[index] == student[idx]:
            if index < idx:
                idx = index

print("{0} {1}".format(scoreAvg, idx+1))