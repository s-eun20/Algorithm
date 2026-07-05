def solution(name, yearning, photo):
    count = {}
    result = []
    
    for i in range(len(name)) :
        count[name[i]] = yearning[i]
        
    for p in photo :
        num = 0
        for word in p :
            if word in count.keys() :
                num += count[word]
        result.append(num)
            
    return result
            