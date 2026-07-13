def solution(ingredient):
    stack = []
    answer = 0
    
    
    for a in ingredient :
        stack.append(a)
        
        if len(stack) >= 4 :
            if stack[-4:] == [1,2,3,1] :
                del stack[-4:]
                answer += 1
        
    return answer