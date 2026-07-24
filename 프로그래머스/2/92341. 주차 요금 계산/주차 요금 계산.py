import math 
def solution(fees, records):
    in_time = {}
    total_time = {}
    total_fee = []
    
    for record in records :
        time,car_number,in_out = record.split()
        hour,minute = map(int,time.split(":"))
        time = hour * 60 + minute
        if in_out == "IN" :
            in_time[car_number] = time
            
        elif in_out == "OUT" :
            inTime = in_time[car_number]
            total_time[car_number] = total_time.get(car_number, 0) + time - inTime
            del in_time[car_number]
            
    out_time = 23*60 + 59 
        
    for car_number,inTime in in_time.items() :
        total_time[car_number] = total_time.get(car_number, 0)+ out_time- inTime
        
        
    for car_number in sorted(total_time):
        parking_time = total_time[car_number]

        if parking_time <= fees[0]:
            money = fees[1]

        else:
            extra_time = parking_time - fees[0]
            extra_count = math.ceil(extra_time / fees[2])

            money = fees[1] + extra_count * fees[3]

        total_fee.append(money)
    return total_fee
        
        