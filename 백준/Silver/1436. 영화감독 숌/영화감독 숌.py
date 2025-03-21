n = int(input())

result = 666
count = 0

while True :
    if '666' in str(result) :
        count +=1
    if count == n :
        print(result)
        break
        
    result+=1