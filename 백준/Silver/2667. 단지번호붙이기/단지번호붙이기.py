import sys
from collections import deque

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, n, area, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1  # 현재 단지 크기 (시작점 포함)

    while queue:
        cx, cy = queue.popleft()  # 현재 좌표
        
        for i in range(4):  # 4방향 탐색
            nx, ny = cx + dx[i], cy + dy[i]

            # 범위 내에 있고, 방문하지 않았으며, 집(1)이 있는 경우
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and area[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1  # 단지 크기 증가

    return count

def solution():
    # 입력 받기
    n = int(sys.stdin.readline().strip())
    area = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
    
    # 방문 체크 배열
    visited = [[False] * n for _ in range(n)]
    
    result = []  # 각 단지의 크기 저장
    
    # 모든 위치를 탐색하며 BFS 실행
    for i in range(n):
        for j in range(n):
            if area[i][j] == 1 and not visited[i][j]:  # 집이 있고 방문하지 않은 경우
                result.append(bfs(i, j, n, area, visited))
    
    # 결과 출력
    print(len(result))  # 단지 수 출력
    print("\n".join(map(str, sorted(result))))  # 단지 크기 오름차순 정렬 후 출력

solution()
