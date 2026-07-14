def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    
    for i, answer in enumerate(answers) :
        if a[i % len(a)] == answer :
            score[0] += 1
        if b[i % len(b)] == answer :
            score[1] += 1
        if c[i % len(c)] == answer :
            score[2] += 1
            
    max_score = max(score)
    
    answer = []
    
    for i,s in enumerate(score) :
        if s == max_score :
            answer.append(i+1)
    return answer
        
    
    answer = []
    return answer