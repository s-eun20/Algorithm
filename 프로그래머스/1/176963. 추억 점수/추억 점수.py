def solution(name, yearning, photo):
    answer = []
    score = {}
    
    for i in range(len(name)) :
        score[name[i]] = yearning[i]
        
    for p in photo :
        total = 0
        for person in p :
            if person in score :
                total += score[person]
        
        answer.append(total)
    return answer