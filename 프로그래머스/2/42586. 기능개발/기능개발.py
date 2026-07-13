def solution(progresses, speeds):
    days = []
    
    for progress,speed in zip(progresses,speeds) :
        remain = 100 - progress
        
        if remain % speed == 0 :
            day = remain // speed
        else :
            day = remain // speed + 1
            
        days.append(day)
    
    answer = []
    
    # 앞 기능을 기준으로 함께 배포되는 개수 계산
    
    current_day = days[0]
    count = 1
    
    for day in days[1:] :
        if day <= current_day :
            count += 1
        else :
            answer.append(count)
            current_day = day
            count = 1
            
    answer.append(count)
    return answer
