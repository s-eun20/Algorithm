import sys

n = int(sys.stdin.readline())
stack = []
result = [] # +,- 저장
current = 1 # 현재 Push 숫자
possible = True # 가능한지 여부

for _ in range(n) :
    target = int(sys.stdin.readline())
    
    while current <= target :
        stack.append(current)
        result.append("+")
        current+=1
    if stack and stack[-1] == target :
        stack.pop()
        result.append("-")
    else :
        possible = False
        break
        
if possible:
    print("\n".join(result))
else :
    print("NO")
        

