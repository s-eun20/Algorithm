def solution(id_list, report, k):
    count = {}
    name = {}
    result = []
    
    for id in id_list:
        count[id] = count.get(id,0)
        name[id] = name.get(id,0)
    
    
    
    report = list(set(report))
    
    for r in report :
        user, target = r.split()
        count[target] +=1
            
    for r in report:
        user, target = r.split()
        
        if count[target] >= k :
            name[user] += 1
            
    
    result = list(name.values())
    return result
            