def solution(num_list):
    even = []
    odd = []
    for num in num_list :
        if num % 2 == 0 :
            even.append(str(num))
        else :
            odd.append(str(num))
    
    result = int(''.join(even) or '0') + int(''.join(odd) or '0') 
    return result