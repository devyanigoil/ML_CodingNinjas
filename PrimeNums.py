import math
def checkPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

n = int(input())
for i in range(2,n+1):
    ans = checkPrime(i)
    if(ans):
        print(i)