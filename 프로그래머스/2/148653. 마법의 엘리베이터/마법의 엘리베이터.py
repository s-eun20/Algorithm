def solution(storey):
    # 그리디란? - 지금 당장 이득인 선택을 하는 것
    # 1의 자리부터 결정하기
    
    answer = 0
    while storey > 0 :
        current = storey % 10
        # 다음 자리 숫자
        next_digit = (storey // 10) % 10
        
        # 현재 자리가 0~4면 내려감
        if current < 5 :
            answer += current
            storey //= 10
        # 현재 자리가 6~9면 올라감
        elif current > 5 :
            answer += 10-current
            storey = (storey // 10 )+1
            
        # 현재 자리가 5면
        else :
            # 다음 자리가 5이상
            if next_digit >= 5 :
                answer += 5
                storey = (storey // 10) +1
            else :
                answer += 5
                storey //= 10
    return answer