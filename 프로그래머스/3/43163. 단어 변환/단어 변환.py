from collections import deque
def solution(begin, target, words):
    
    visited = [False] * len(words)
    queue = deque()
    queue.append((begin,0))
    
    while queue :
        current,count = queue.popleft()
        
        if current == target :
            return count
        for i in range(len(words)) :
            if visited[i] :
                continue
                
            diff = 0
            
            for a,b in zip(current,words[i]) :
                if a!=b :
                    diff += 1
                    
            if diff == 1 :
                visited[i] = True
                queue.append((words[i],count+1))
                
    return 0
    