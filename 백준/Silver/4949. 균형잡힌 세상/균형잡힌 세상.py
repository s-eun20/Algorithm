import sys
while True :
    string = sys.stdin.readline().rstrip()
    stack = []
    is_vaild = True
    
    if string == "." :
        break
    for ch in string :
        if ch == "(" or ch == "[":
            stack.append(ch)
        elif ch == ")" :
            if not stack or stack[-1] != "(" :
                is_vaild = False
                break
            stack.pop()
            
            
        elif ch == "]" :
            if not stack or stack[-1] != "[" :
                is_vaild = False
                break
            stack.pop()
     
    if is_vaild and not stack :
        print("yes")
    else :
        print("no")
        
                
     