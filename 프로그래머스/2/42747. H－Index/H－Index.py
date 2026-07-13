def solution(citations):
    citations.sort(reverse = True)
    
    h_index = 0 
    
    for i,citation in enumerate(citations) :
        paper_count = i+1
        
        if citation >= paper_count :
            h_index = paper_count
        else :
            break
            
    return h_index
    
    
    