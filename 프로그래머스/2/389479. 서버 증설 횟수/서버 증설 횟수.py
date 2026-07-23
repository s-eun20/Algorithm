def solution(players, m, k):
    
    # m <= 이면 서버 +1 서버가 증설되면, k시간 동안 유효하다
    # 서버가 (n*m) <= 서버수 최소 n대이상 < (n+1) *m
    # 현재 있는 서버 / 증설 횟수 따로 저장.. 
    # 한시간 마다 필요한 서버 갯수를 계산해야함 현재 필요한 서버갯수 = players[i] / m if 나머지가 있으면  += 1
    # 현재 필요한 서버갯수랑 현재 있는 서버를 비교 -> 부족하면 현재 있는 서버 늘리고, 그에 따른 증설 횟수도 늘려야함..
    # 문자열로 저장을 해야되나 현재 있는 서버를? 
    current = 0
    expire = [0] * (len(players)+k)
    count = 0
    for i in range(len(players)) :
        #1. 현재 시간에 만료되는 서버를 먼저 제거
        current -= expire[i]
        needs = players[i] // m
        
        if current < needs :
            
            add = needs - current
            current += add
            count += add
            
            expire[i+k] += add
        
        
    return count