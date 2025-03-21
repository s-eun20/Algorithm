n = int(input())

result = 1
for i in range(2, n + 1): 
    result *= i
    
    
total_str = str(result)[::-1] 

count = 0
for i in total_str:
    if i == '0':
        count += 1  
    else:
        break  

print(count)

    