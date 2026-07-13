from heapq import heappush, heappop,heapify
def solution(scoville, K):
    
    heapify(scoville)
    
    count = 0
    
    while scoville and scoville[0] < K : 
        
        if len(scoville) < 2 :
            return -1 
        first = heappop(scoville)
        second = heappop(scoville)
        
        new = first + (second * 2)
        
        heappush(scoville, new)
        
        count += 1
        
    return count
    