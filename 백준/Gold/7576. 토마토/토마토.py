from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(box, n, m):
    queue = deque()
    
    # 모든 익은 토마토(1) 위치를 큐에 추가
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j))
    
    days = -1  # 처음부터 1일이 아니라, 처음 상태도 0일로 포함

    while queue:
        days += 1
        for _ in range(len(queue)):  # 현재 날짜의 모든 토마토 탐색
            x, y = queue.popleft()

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]

                if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                    box[nx][ny] = 1  # 익은 토마토로 변경
                    queue.append((nx, ny))

    return days

def solution():
    m, n = map(int, sys.stdin.readline().split())  # 주의: (n, m) 순서
    box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # BFS 실행하여 모든 토마토가 익는 데 걸리는 날짜 구하기
    days = bfs(box, n, m)

    # 모든 토마토가 익었는지 확인
    for row in box:
        if 0 in row:  # 아직 익지 않은 토마토가 있다면 -1 반환
            print(-1)
            return

    print(days)

solution()
