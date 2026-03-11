n,s = map(int,input().split())
num = list(map(int,input().split()))

count = 0 
def dfs(idx,total):
    global count
    
    if idx == n :
        if total == s:
            count += 1
        return
    
    dfs(idx+1, total + num[idx])
    dfs(idx+1, total)
dfs(0,0)

if s == 0 :
    count -= 1
        
print(count)