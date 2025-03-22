import math

def is_prime(n):
    if n < 2 :
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
    
N = int(input())
primes = list(map(int,input().split()))
count = sum(1 for num in primes if is_prime(num))
print(count)
              
              