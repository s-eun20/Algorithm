def solution(arr):
    answer = []
    
    for number in arr :
        if len(answer) == 0 :
            answer.append(number)
        elif number != answer[-1] :
            answer.append(number)
        
        
    return answer