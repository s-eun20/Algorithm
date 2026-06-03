def solution(babbling):
    answer = 0
    possible = ["aya","ye","woo","ma"]
    
    for babble in babbling :
        for word in possible:
            if word*2 in babble:
                break
        else :
            for word in possible:
                babble = babble.replace(word," ")
            if babble.strip() == "":
                answer += 1
                
    return answer
        
            
            
    return answer

# 두번 검사를 해야하나