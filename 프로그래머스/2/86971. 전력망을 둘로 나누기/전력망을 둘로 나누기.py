def dfs(node,n,wires,visited,cut) :
    visited[node] = True
    
    
    for i , (a,b) in enumerate(wires) :
        
        # 이번에 끊은 전선은 무시
        if i == cut :
            continue
        
        #node와 연결된 송전탑을 찾음
        if a == node and not visited[b] :
            dfs(b,n,wires,visited,cut)
            
        elif b == node and not visited[a] :
            dfs(a,n,wires,visited,cut)
def solution(n, wires):
    answer = n
    
    # 전선 하나씩 끊어보기
    
    for cut in range(len(wires)) :
        visited = [False] * (n+1)
        
        # 1번 송전탑에서 시작해서 연결된 송전탑 갯수 세기
        
        dfs(1,n,wires,visited,cut)
        
        count = 0
        
        for i in range(1,n+1) :
            if visited[i] :
                count += 1
        # 나머지 송전탑 개수
        other = n - count
        
        # 두 그룹 차이
        diff = abs(count - other)
        
        answer = min(answer,diff)
        
    return answer

# 전력망을 둘로 나누는 기준은? -> 송전탑 갯수가 비슷하게 -> 그렇게 나눌려면?
# 하나씩 끊어보고 갯수를 세어봐야 하나



    

    # 끊을 전선을 제외하고 연결 상태 만들기

    # DFS/BFS로 한쪽 송전탑 개수 세기

    # 다른 쪽 = n - count

    # 차이 계산

    # 가장 작은 차이 저장