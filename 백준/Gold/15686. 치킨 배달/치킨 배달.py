from itertools import combinations

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            houses.append((i, j))
        elif grid[i][j] == 2:
            chickens.append((i, j))

def city_chicken_distance(selected_chickens):
    total = 0
    for hx, hy in houses:
        best = 10**18
        for cx, cy in selected_chickens:
            dist = abs(hx - cx) + abs(hy - cy)
            if dist < best:
                best = dist
        total += best
    return total

answer = 10**18
for comb in combinations(chickens, M):
    answer = min(answer, city_chicken_distance(comb))

print(answer)
