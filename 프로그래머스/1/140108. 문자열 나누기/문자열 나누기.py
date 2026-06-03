def solution(s):
    answer = 0
    
    same = 0
    diff = 0
    x = ''
    
    for char in s :
        if same == 0 and diff == 0 :
            x = char
            
        if x == char :
            same += 1
        else :
            diff += 1
        
        if same == diff :
            answer += 1
            same = 0
            diff = 0
        
    if same != 0 or diff != 0 :
        answer += 1
    
    return answer
            