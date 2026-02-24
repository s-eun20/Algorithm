import sys
num = int(sys.stdin.readline())


for _ in range(num) :
    stack = []
    string = sys.stdin.readline().strip()
    is_vaild = True
    
    for j in string :
        if j == "(" :
            stack.append(j)
        elif j == ")" :
            if not stack:
                is_vaild = False
                break
            stack.pop()
           
    if is_vaild and not stack :
        print("YES")
    else :
        print("NO")
    

