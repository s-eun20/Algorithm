def solution(n,a,b):
    answer = 0
    
    while a != b :
        
        a = (a+1) // 2
        b = (b+1) // 2
        answer += 1
        
    

    return answer


#붙게되는 숫자 중 짝수면 절반이 다음 순위 홀수면 +1 나누기 2

# 첫번째 4번->3번 4번이 2번 / 7번->8번 7번은 4번
# 2번은 1번 / 4