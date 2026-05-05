def solution(num_list):
    mul = 1 
    plu = 0
    for i in num_list :
        mul *=i
        plu +=i
    
    if mul < plu * plu :
        return 1
    else : return 0
        