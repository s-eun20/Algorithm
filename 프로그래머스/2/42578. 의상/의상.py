def solution(clothes):
    type = {}
    answer = 1
    
    for cloth in clothes :
        if cloth[1] in type :
            type[cloth[1]] +=1
        else :
            type[cloth[1]] =1
        
    for key,value in type.items() :
        answer *= value+1
        
    return answer - 1
               
    