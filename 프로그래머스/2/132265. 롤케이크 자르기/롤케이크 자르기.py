def solution(topping):
    answer = 0
    #slice를 해야하는건가 딕셔너리는 어캐쓰지
    # 공평한지 어캐 비교?? -> len(topping) // 2 개 기준으로 배열을 나눠야 하나? 
    # 딕셔너리에 각 숫자가 몇개인지 저장하고 비교??
    
    left = set()
    right = {}
    
    for top in topping :
        right[top] = right.get(top,0) + 1
        
    # 토핑을 왼쪽으로 하나씩 이동
    
    for x in topping :
        left.add(x)
        
        right[x] -= 1
        
        # 오른쪽 종류가 다 사라지면 삭제해야함
        if right[x] == 0 :
            del right[x]
            
        # 왼쪽과 오른쪽 토핑 수 비교
        if len(left) == len(right) :
            answer += 1
            
    return answer
        
    