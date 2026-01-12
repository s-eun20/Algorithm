from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

def team_score(team):
    score = 0
    for x in range(len(team)):
        for y in range(x + 1, len(team)):
            i, j = team[x], team[y]
            score += S[i][j] + S[j][i]
    return score

all_people = set(range(N))
ans = 10**18

# 0번을 스타트팀에 고정해서 중복 탐색 절반 제거
for comb in combinations(range(1, N), N // 2 - 1):
    start = (0,) + comb
    link = list(all_people - set(start))
    ans = min(ans, abs(team_score(start) - team_score(link)))

print(ans)
