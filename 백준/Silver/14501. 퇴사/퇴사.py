
N = int(input())
T=[0]*N
P=[0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())


ans = 0

def dfs(day,money) :
    global ans
    if day >= N : # day가 N보다 크거나 같으면
        ans = max(ans, money) # 최댓값 저장 후 리턴
        return

    if day + T[day] <= N: # 상담을 하기로 하는 경우(N보단 작아야함)
        dfs(day+T[day],money + P[day]) # money만 더함

    dfs(day+1,money) # 상담안하면 다음 날로 넘어감

dfs(0,0)
print(ans)