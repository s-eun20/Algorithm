def solution(s):
    stack = []
    
    for word in s :
        if not stack or word == "(" :
            stack.append(word)
        else :
            stack.pop()
        
    if not stack:
        return True
    else :
        return False