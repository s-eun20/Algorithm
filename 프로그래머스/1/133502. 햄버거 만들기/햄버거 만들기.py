def solution(ingredient):
    answer = 0
    stack = []
    
    for a in ingredient :
        stack.append(a)
        
        if stack[-4:] == [1,2,3,1] :
            answer += 1
            del stack[-4:]
    
    return answer
        
        



