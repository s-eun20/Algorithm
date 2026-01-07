def solution(sizes):
    width = 0
    length = 0
    
    for w,h in sizes :
        width = max(width, max(w,h))
        length = max(length,min(w,h))
    
    return width*length

