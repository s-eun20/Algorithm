n= int(input())
num = list(map(int,input().split()))
x = int(input())
num.sort()

left = 0
right = n-1
count = 0

while left < right :
    s = num[left] + num[right]
    
    if s == x :
        count +=1
        left += 1
        right -= 1
    elif s < x :
        left += 1
    else :
        right -= 1
        
print(count)
