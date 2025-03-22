num = int(input())

result = 0

for i in range(num):
    sum_d = sum(map(int,str(i)))
    
    if i + sum_d == num :
        result = i
        break
        
        
print(result)
    
    
    