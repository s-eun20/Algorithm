import heapq
def solution(n, k, enemy):
    # 가장 많은 적이 있을 때 -> 무적권
    # 병사를 먼저 사용해서 라운드를 진행 -> 병사 부족 -> 지금까지 지나온 라운드 중 적이 가장 많았던 라운드에 무적권 사용
    heap = []
    
    for round_number,enemy_count in enumerate(enemy):
        n -= enemy_count
        heapq.heappush(heap,-enemy_count)
        
        if n < 0 :
            if k == 0 :
                return round_number
            largest_enemy = - heapq.heappop(heap)
            n += largest_enemy
            k -= 1
            
    return len(enemy)