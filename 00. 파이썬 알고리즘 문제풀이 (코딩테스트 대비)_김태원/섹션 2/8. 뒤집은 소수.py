n = int(input())
num = list(map(int, input().split()))

def reverse(x):
    mNum = str(x)
    mReverseNum = "".join(reversed(mNum))

    return int(mReverseNum)

def isPrime(x):
    ans = list()

    for v in x:
        mIsPrime = True
        mNum = reverse(v)

        if mNum == 1:
            continue
        
        for i in range(2, mNum):
            if mNum % i == 0:
                mIsPrime = False
                break
        
        if mIsPrime == True:
            ans.append(mNum)

    return ans

print(*isPrime(num))