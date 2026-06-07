def solution(a, b, n):
    answer = 0
    
    while n >= a :
        receive = (n // a) * b 
        current = n - (n // a) * a + receive
        answer += receive
        n = current
        
    return answer
