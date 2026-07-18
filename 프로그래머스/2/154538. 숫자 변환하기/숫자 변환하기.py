from collections import deque
def solution(x, y, n):
    queue = deque()
    queue.append((x,0))
    
    visited = [False] * (y+1)
    visited[x] = True
    
    while queue :
        num,cnt = queue.popleft()
        
        if num == y :
            return cnt
        
        for nxt in (num+n,num*2,num*3) :
            if nxt <=y and not visited[nxt] :
                visited[nxt] = True
                queue.append((nxt,cnt+1))
                
                
    return -1