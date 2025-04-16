from collections import deque

N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
for _ in range(K) :
    x,y = map(int, input().split())
    board[x-1][y-1] = 1

L = int(input())
dic = {}

for _ in range(L) :
    t,c = input().split()
    dic[int(t)] = c
    
snake = deque()

snake.append((0,0))

dir = 0
time = 0
x,y = 0,0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

while True :
    time += 1
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    if nx<0 or nx >= N or ny<0 or ny>=N or (nx,ny) in snake :
        break
        
    if board[nx][ny] == 1 :
        board[nx][ny] = 0
        snake.append((nx,ny))
    else :
        snake.append((nx,ny))
        snake.popleft()
        
        
    if time in dic :
        if dic[time] == 'L':
            dir = (dir-1) % 4
        else :
            dir = (dir+1) % 4
            
    x,y = nx,ny
    
print(time)    