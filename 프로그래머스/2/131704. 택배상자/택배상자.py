def solution(order):
    stack = []
    current = 1
    count = 0
    
    for target in order:
        while current <= target :
            stack.append(current)
            current += 1
        if stack and stack[-1] == target:
            stack.pop()
            count += 1
        else :
            break
            
    
        
    return count