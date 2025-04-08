import sys
input = sys.stdin.readline

# 북, 동, 남, 서 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())  # 방 크기
x, y, d = map(int, input().split())  # 시작 위치, 방향
room = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]  # 청소 여부 저장
count = 0

while True:
    # 1. 현재 위치 청소
    if room[x][y] == 0 and visited[x][y] == 0:
        visited[x][y] = 1
        count += 1

    turned = False  # 회전해서 이동했는지 여부

    # 2. 4방향을 차례대로 확인
    for _ in range(4):
        d = (d + 3) % 4  # 반시계 방향 회전
        nx = x + dx[d]
        ny = y + dy[d]

        if room[nx][ny] == 0 and visited[nx][ny] == 0:
            # 청소되지 않은 공간이 있다면 이동
            x, y = nx, ny
            turned = True
            break

    if not turned:
        # 3. 후진 시도
        back = (d + 2) % 4
        bx = x + dx[back]
        by = y + dy[back]

        if room[bx][by] == 1:
            break  # 뒤가 벽이면 작동 종료
        else:
            x, y = bx, by  # 뒤로 이동

print(count)
