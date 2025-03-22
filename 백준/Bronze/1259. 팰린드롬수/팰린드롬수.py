while True :
    num = int(input())
    
    if num == 0 :
        break
        
    num2 = int(str(num)[::-1])
    
    if num == num2 :
        print("yes")
    else :
        print("no")
        
    