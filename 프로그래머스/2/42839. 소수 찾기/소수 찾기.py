from itertools import permutations

def isPrime(num) :
    
    if num < 2 :
        return False
    
    for i in range(2, int(num ** 0.5) + 1) :
        
        if num % i == 0 :
            return False
        
    return True
            
def solution(numbers):
    answer = set()
    for i in range(1, len(numbers) + 1) :
        
        for p in permutations(numbers,i) :
            num = int(''.join(p))
            
            if isPrime(num) :
                answer.add(num)
                
    return len(answer)
    
        
