n = int(input())
student = list(map(int, input().split()))

scoreAvg = round(sum(student) / n)
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