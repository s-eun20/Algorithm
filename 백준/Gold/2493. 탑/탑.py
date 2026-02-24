import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = []          # 인덱스를 저장할 스택
ans = [0] * N       # 정답 배열 (기본값 0)

for i in range(N):
    # 나보다 낮은 탑들은 제거 (레이저 못 막음)
    while stack and A[stack[-1]] < A[i]:
        stack.pop()

    # 스택이 비어있지 않으면
    # stack[-1]이 나를 막아줄 가장 가까운 탑
    if stack:
        ans[i] = stack[-1] + 1  # 문제는 1번부터 시작

    # 현재 탑을 스택에 추가
    stack.append(i)

print(*ans)