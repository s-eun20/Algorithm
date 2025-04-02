import sys
from collections import deque

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

def bfs(area,visited,x,y,n,m):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(8):
            nx,ny = x+dx[i],y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if area[nx][ny] == 1:
                    queue.append((nx,ny))
                    visited[nx][ny] = True

while True:
    m,n = map(int,sys.stdin.readline().split())
    if n==0 and m==0:
        break
    area = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    visited = [[False]*m for _ in range(n)] 
    
    count = 0
    for i in range(n):
        for j in range(m):
            if area[i][j] == 1 and not visited[i][j]:
                bfs(area,visited,i,j,n,m)
                count +=1
    
    print(count)
    
                
    
            