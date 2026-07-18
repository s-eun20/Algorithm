def solution(x, y, n):
    INF = 1000001
    
    dp = [INF] * (y+1)
    dp[x] = 0
    
    for i in range(x,y+1) :
        if dp[i] == INF :
            continue
        
        if i + n <= y :
            dp[i+n] = min(dp[i+n], dp[i] + 1)
            
        if i*2 <= y :
            dp[i*2] =min(dp[i*2], dp[i] + 1)
            
        if i * 3 <= y :
            dp[i*3] =min(dp[i*3], dp[i] + 1)
            
    return dp[y] if dp[y] != INF else -1
    
    # 최소 - > bfs !!!!
    # 이문제는 dp가 더 유명
    # 이미 계산한 결과를 저장해서 다시 계산하지 않는 것
    # if x = 10, y = 40, n = 5
    # dp[10] = 0 dp[15] = 1, dp[20] = 1, dp[30] = 1
