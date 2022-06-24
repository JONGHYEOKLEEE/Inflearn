# in1 : 8 4     / out1 : 8
# in2 : 25 5    / out2 : -1
# in3 : 100 5   / out3 : 10
# in4 : 100 7   / out4 : 25
# in5 : 1000 12 / out5 : 125

n, k = map(int, input().split())
divisorList = list()

for i in range(1, n+1):
    divisor = n%i

    if divisor == 0:
        divisorList.append(i)

if k > len(divisorList):
    print(-1)
else:
    print(divisorList[k-1])