def solution(participant, completion):
    
    parts = {}

    for part in participant:
        parts[part] = parts.get(part,0) + 1

    for person in completion:
        parts[person] -= 1
        
    for key,value in parts.items():
        if value == 1 :
            return key