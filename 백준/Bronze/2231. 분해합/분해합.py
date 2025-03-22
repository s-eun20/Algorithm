num = int(input())

result = 0

for i in range(1,num):
    d_sum = sum(map(int,str(i)))
    
    if i + d_sum == num :
        result = i
        break
        
print(result)