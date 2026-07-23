def solution(a, b):
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    # 92+29 = 121
    week = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    # 전 월의 날짜를 모두 더한다 -> 
    days = 0
    for i in range (a-1) :
        days += months[i]
        
    days += b-1
    return week[days%7]