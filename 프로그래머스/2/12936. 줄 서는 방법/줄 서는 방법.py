from math import factorial
def solution(n, k):
    #K가 몇 번째 묶음에 들어가는지를 구하는게 포인트
    people = list(range(1,n+1))
    answer = []
    
    #k를 0부처 시작하는 번호로 변경
    k -= 1
    while people :
        # 현재 자리를 하나 정했을 때 생기는 순열의 갯수
        group_size = factorial(len(people) - 1)
        
        #k가 몇 번째 묶음에 들어가는지 계산
        index = k // group_size
        
        #해당 사람을 정답에 추가하고 남은 목록에서 제거
        answer.append(people.pop(index))
        
        # 선택한 묶음 안에서 몇 번째인지 계산
        k %= group_size
        
    return answer