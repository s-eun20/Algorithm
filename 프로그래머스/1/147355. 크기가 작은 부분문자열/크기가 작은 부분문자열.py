def solution(t, p):
    #반복문을 돌면서 len(p) 만큼 슬라이싱?
    # if int(p)보다 크면 count += 1
    count = 0
    
    for i in range ((len(t)- len(p)+1)) :
        length = len(p) + i
        if int(p) >= int(t[i:length]) :
            count += 1
    
    return count
    