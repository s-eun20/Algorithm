def solution(phone_book):
    
    dic  = {}
    
    for phone_number in phone_book :
        dic[phone_number] = True
    
    for number in phone_book :
        for i in range(1,len(number)) :
            if number[:i] in dic :
                return False
    return True