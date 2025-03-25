import math
N,M = map(int,input().split())


def isPrime(num):
    if num<2 :
        return False
    for i in range(2, int(math.sqrt(num))+1) :
        if num%i==0 :
            return False
    return True
            

for i in range(N,M+1) :
    if isPrime(i) :
        print(i)
    


    