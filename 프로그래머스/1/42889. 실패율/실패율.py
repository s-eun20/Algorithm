def solution(N, stages):
    # 딕셔너리 - stage 번호 : 클리어하지못한사용자
    number = {}
    answer = {}
    
    # number (1,1), (2,3),(3,2),(4,1),(5,0)
    
    
    for stage in stages :
        number[stage] = number.get(stage,0) + 1
        
    deno = len(stages)
    for i in range(1,N+1) :
        if deno == 0 :
            answer[i] = 0
        else :
            answer[i] = number.get(i,0) / deno
        
        deno -= number.get(i,0)
            
    result = sorted(answer.items(), key=lambda x:x[1] ,reverse=True)
    return [stage for stage, fail in result]