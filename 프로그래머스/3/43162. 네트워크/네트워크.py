from collections import deque
def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    for start in range(n) :
        if visited[start] :
            continue
            
        queue = deque([start])
        visited[start] = True
        answer += 1
        
        while queue :
            current = queue.popleft()
            
            for next_computer in range(n) :
                if computers[current][next_computer] ==1 :
                    if not visited[next_computer] :
                        visited[next_computer] = True
                        queue.append(next_computer)
    return answer