def solution(plans):
    #1. 시작 시간을 기준으로 정렬
    plans.sort(key=lambda x:x[1])
    
    #2. 분 단위로 변환하는 함수
    def time_to_minutes(time):
        h,m = map(int,time.split(":"))
        return h*60+m
    
    
    stack = []
    result = []
    current_time=0
    
    for i in range(len(plans)):
        name,start,playtime = plans[i]
        start = time_to_minutes(start)
        playtime = int(playtime)
        
        #4. 이전 과제 진행(멈춘 과제 이어서 수행)
        while stack and current_time < start:
            prev_name, remaining_time = stack.pop()
            time_gap = start-current_time
            
            if remaining_time <= time_gap:
                #현재 시간 내에 과제 완료 가능
                result.append(prev_name)
                current_time += remaining_time
            else :
                stack.append((prev_name,remaining_time - time_gap))
                current_time = start
                break
                
        #5. 새로운 과제 시작
        current_time = start+playtime
        if i <len(plans) - 1 and current_time > time_to_minutes(plans[i+1][1]) :
        # 다음 과제 시작 시간 전에 끝내지 못하면 스택에 저장
            stack.append((name,current_time-time_to_minutes(plans[i+1][1])))
            current_time = time_to_minutes(plans[i+1][1])
        else :
            result.append(name)
    while stack:
        result.append(stack.pop()[0])
        
    return result
        