def solution(code):
    result = []
    mode = 0
    for i in range(len(code)):
        if code[i] == "1":
            if mode == 0:
                mode = 1
            else :
                mode = 0
        if mode == 0 and i%2==0 and code[i]!="1":
            result.append(code[i])
        elif mode == 1 and i%2 !=0 and code[i]!="1" :
            result.append(code[i])
            
    if not result :
        return "EMPTY"
        
    return ''.join(result)