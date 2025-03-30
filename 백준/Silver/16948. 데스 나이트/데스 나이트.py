import sys 
from collections import deque

dx =[-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs(N,r1,c1,r2,c2):
    queue = deque([(r1,c1,0)])
    visited = [[False]*N for _ in range(N)]
    visited[r1][c1] = True
    
    while queue:
        x,y,count = queue.popleft()
        
        if x == r2 and y==c2:
            return count
        
        for i in range(6):
            nx,ny = x+dx[i],y+dy[i]
            
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny,count+1))
    return -1
def solution():
    N = int(sys.stdin.readline())
    r1,c1,r2,c2 = map(int,sys.stdin.readline().split())
    
    print(bfs(N,r1,c1,r2,c2))
solution()