from itertools import combinations
def solution(n, q, ans):
    answer = 0
    candidates = list(combinations(range(1,n+1),5))
    
    for code in candidates :
        
        possible = True
        
        for i in range(len(q)) :
            
            # 공통 숫자 개수
            cnt = len(set(code) & set(q[i]))
            
            if cnt != ans[i] :
                possible = False
                break
                
        if possible :
            answer += 1
            
    return answer
        
        