def add_time(time) :
    hour = time // 100
    minute = time % 100
    
    minute += 10
    
    if minute >= 60 :
        hour += 1
        minute -= 60
    return hour*100 +minute
def solution(schedules, timelogs, startday):
    
    #시에 100을 곱하고 분을 더함.. 
    # startday가 -> 시작날 
    answer = 0
    
    for i in range(len(schedules)) :
        limit = add_time(schedules[i])
        success = True
        
        for day in range(7) :
            #주말 검사 안함
            weekday = (startday+day - 1) % 7 
            if weekday >= 5 :
                continue
                
            if timelogs[i][day] > limit :
                success = False
                break
            
        if success :
            answer += 1
    return answer