def solution(weights):
    weights.sort()
    count = {}
    answer = 0
    
    for w in weights :
        # 같은 무게 확인
        answer += count.get(w,0)
        
        #앞사람 : 현재사람 = 2:3
        if w % 3 == 0 :
            answer += count.get(w*2 // 3,0)
        
        # 2:4
        if w % 2 == 0 :
            answer += count.get(w//2  , 0)
        # 3 : 4 
        if w % 4 == 0 :
            answer += count.get(w*3 // 4,0)
        
        # 현재 사람 저장
        count[w] = count.get(w,0) + 1
    return answer