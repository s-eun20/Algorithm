import sys
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x1,y1,campus,visited,N,M):
    queue = deque()
    queue.append((x1,y1))
    visited[x1][y1] = True
    
    count = 0
    
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if campus[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    if campus[nx][ny] == 'P':
                        count += 1
    return count                    

def solution():
    N,M = map(int,sys.stdin.readline().split())
    campus = [list(sys.stdin.readline().strip()) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    
    people = 0
    
    for i in range(N):
        for j in range(M):
            if campus[i][j] == 'I' and not visited[i][j]:
                people = bfs(i,j,campus,visited,N,M)
   
    print("TT" if people == 0 else people)
    
    
    
solution()