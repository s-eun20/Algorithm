def solution(keymap, targets):
    dic = {}
    result = []
    
    for key in keymap :
        for i,ch in enumerate(key) :
            if ch in dic :
                dic[ch] = min(dic[ch], i+1)
            else :
                dic[ch] = i + 1
    
    for target in targets :
        sum = 0
        for t in target :
            if t not in dic :
                sum = -1
                break
            sum += dic[t]
        result.append(sum)
        
    
    return result