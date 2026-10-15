def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    
    def dfs(current,count) :
        nonlocal answer
        
        answer = max(answer,count) 
        
        for i in range(len(dungeons)) :
            
            if visited[i] :
                continue
            
            if current < dungeons[i][0] :
                continue
                
            visited[i] = True
            
            dfs(current - dungeons[i][1],count+1)
            
            visited[i] = False
            
    dfs(k,0)
    return answer