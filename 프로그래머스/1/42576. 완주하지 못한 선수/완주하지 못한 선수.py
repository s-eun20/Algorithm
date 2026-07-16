
def solution(participant, completion):
    answer = {}
    
    for part in participant :
        answer[part] = answer.get(part,0) + 1
        
    for name in completion :
        answer[name] -= 1
        
    for key,value in answer.items() :
        if value > 0  :
            return key