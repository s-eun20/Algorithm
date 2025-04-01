import sys
from collections import deque

T = int(sys.stdin.readline())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,N,M,ground,visited):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue :
        a,b = queue.popleft()
        
        for i in range(4):
            nx,ny = a+dx[i],b+dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and ground[nx][ny]==1:
                visited[nx][ny]=True
                queue.append((nx,ny))

for _ in range(T):
    M,N,K = map(int,sys.stdin.readline().split())
    ground = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    
    for i in range(K):
        x,y = map(int,sys.stdin.readline().split())
        ground[y][x] = 1
        
    worm_count = 0
    
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1 and not visited[i][j]:
                bfs(i,j,N,M,ground,visited)
                worm_count+=1
    print(worm_count)