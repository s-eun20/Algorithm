def solution(players, callings):
    rank = {}
    answer = []
    
    for i in range(len(players)) :
        rank[players[i]] = i
    
    for calling in callings :
        idx = rank[calling]
        front = players[idx-1]
        players[idx] = front
        players[idx-1] = calling
        rank[calling] -=1
        rank[front] += 1
    
    
    return players