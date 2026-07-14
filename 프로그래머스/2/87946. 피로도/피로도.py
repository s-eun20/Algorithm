from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for order in permutations(dungeons) :
        remain = k
        count = 0
        
        for required, cost in order :
            if remain >= required :
                remain -= cost
                count += 1
            else :
                break
        answer = max(answer, count)
        
    return answer
    
    # 처음에 dungeons[0] >= k 이어야 시작 가능 -> 정렬을 해야하나???
    # 그 다음으로 올 수 있는 모든 경우의 수를 반복해야함...