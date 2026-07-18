def solution(k, tangerine):
    
    # k개를 고르는데 서로 다른 종류는 많이 안골라야함
    # 사이즈별 갯수 딕셔너리 만들고 최소한으로 뽑아야하나?
    # 젤 많은 갯수를 가진 크기부터 다 뽑고 그다음 ~
    # 조합의 갯수는 어캐 구한담??
    
    count = {}
    
    for x in tangerine :
        count[x] = count.get(x,0) + 1
        
    counts = sorted(count.values(), reverse=True)
    selected = 0
    answer = 0
    
    #갯수가 많은 것부터 선택
    for amount in counts :
        selected += amount
        answer += 1
        
        if selected >= k :
            break
    return answer