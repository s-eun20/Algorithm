num = int(input())

result = 0

for i in range(num):
    sum_d = sum(map(int,str(i)))
    
    if sum_d + i == num :
        result = i
        break

print(result)
    