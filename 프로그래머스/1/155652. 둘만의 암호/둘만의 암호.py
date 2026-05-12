def solution(s, skip, index):
    alphabet = [chr(code) for code in range(97,123)]
    
    #skip에 없는 알파벳만 남기기
    usable = []
    for alpha in alphabet :
        if alpha not in skip :
            usable.append(alpha)
            
    answer = ''
    for alpha in s:
        current_idx = usable.index(alpha)
        new_idx = (current_idx + index) %len(usable)
        answer += usable[new_idx]
        
    return answer
        