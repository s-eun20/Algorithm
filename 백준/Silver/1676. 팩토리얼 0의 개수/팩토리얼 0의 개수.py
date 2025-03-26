n = int(input())

count = 0
def factorial(n):
    if n >1 :
        return n*factorial(n-1)
    else :
        return 1
    
num = str(factorial(n))[::-1]

for i in num :
    if i == '0':
        count+=1
    else :
        break
        
print(count)

