def solution(s):
    answer = 0
    
    for _ in range(len(s)) :
        stack = []
        
        #괄호 하나씩 검사
        for ch in s :
            if ch in "([{":
                stack.append(ch)
            
            #닫는 괄호면
            else :
                if not stack :
                    break
                
                if ch == ")" and stack[-1] == "(" :
                    stack.pop()
                elif ch == "]" and stack[-1] == "[" :
                    stack.pop()
                elif ch == "}" and stack[-1] == "{" :
                    stack.pop()
                    
                else :
                    break
                    
        else : 
            if not stack :
                answer += 1
        s = s[1:] + s[0]
            
    return answer