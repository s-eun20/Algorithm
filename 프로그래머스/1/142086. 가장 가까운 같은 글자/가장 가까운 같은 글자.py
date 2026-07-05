def solution(s):
    words = {}
    result = []
    
    for i,word in enumerate(s) :
        if word in words :
            result.append(i - words[word])
        else:
            result.append(-1)
            
        words[word] = i
        
    return result
    