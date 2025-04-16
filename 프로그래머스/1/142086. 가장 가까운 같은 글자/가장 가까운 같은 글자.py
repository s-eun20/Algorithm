def solution(s):
    last = {}
    result = []
    
    for i, char in enumerate(s) :
        if char in last :
            result.append(i-last[char])
        else :
            result.append(-1)
        last[char] = i
        
        
    return result