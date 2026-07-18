from collections import deque
def solution(begin, target, words):
    queue = deque()
    queue.append((begin,0))
    
    visited = [False] * len(words)
    
    while queue :
        current, count = queue.popleft()
        
        if current == target :
            return count
        
        for i in range(len(words)) :
            if visited[i] :
                continue
                
            different = 0
            
            for a,b in zip(current, words[i]):
                if a != b :
                    different += 1
                    
            if different == 1 :
                visited[i] = True
                queue.append((words[i],count+1))
    return 0
