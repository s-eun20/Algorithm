n = int(input())
stack = []
result = []
current = 1
possible = True
for _ in range(n):
    num = int(input())
    
    while current <= num:
        stack.append(current)
        result.append("+")
        current +=1
        
        
    if stack[-1] == num :
        stack.pop()
        result.append("-")
    else:
        possible = False
        break
    
if possible :
    print("\n".join(result))
else :
    print("NO")
        