def solution(survey, choices):
    answer = ""
    
    score = {
    "R": 0,
    "T": 0,
    "C": 0,
    "F": 0,
    "J": 0,
    "M": 0,
    "A": 0,
    "N": 0
}
    
    for s,choice in zip(survey,choices) :
        left = s[0]
        right = s[1]
        
        
        if choice < 4 :
            score[left] += 4 - choice
        elif choice > 4 :
            score[right] += choice - 4
        
    types = ["RT", "CF", "JM", "AN"]
        
    for t in types:
        left = t[0]
        right = t[1]
            
        if score[left] >= score[right] :
            answer += left
        else :
            answer += right
                
    return answer            
        