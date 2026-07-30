def solution(want, number, discount):
    buy = {}
    count = 0
    
    for fruit,num in zip(want,number) :
        buy[fruit] = num
        
    for start in range(len(discount)) :
        temp = buy.copy()
        window = discount[start:start+10]
        
        for fruit in window :
            if fruit in temp :
                temp[fruit] -= 1
        
        if all(value == 0 for value in temp.values()) :
            count += 1
            
    return count