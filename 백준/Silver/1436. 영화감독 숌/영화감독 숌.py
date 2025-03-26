N = int(input())

result = 666

count = 0

while True :
    if '666' in str(result):
        count +=1     
        if count == N :
            print(result)
            break
    result += 1
     