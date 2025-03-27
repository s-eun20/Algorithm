from functools import lru_cache

def solution(info, n, m):
    @lru_cache(None)  # 중복 연산 방지
    def dfs(idx, a_trace, b_trace):
        if a_trace >= n or b_trace >= m:
            return float('inf')

        if idx == len(info):
            return a_trace

        pick_A = dfs(idx + 1, a_trace + info[idx][0], b_trace)
        pick_B = dfs(idx + 1, a_trace, b_trace + info[idx][1])

        return min(pick_A, pick_B)

    answer = dfs(0, 0, 0)
    return answer if answer != float('inf') else -1
