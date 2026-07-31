from itertools import combinations
def solution(orders, course):
    answer = []
    
    for c in course :
        count = {}
        
        for order in orders :
            order = sorted(order)
            for comb in combinations(order,c) :
                menu = ''.join(comb)
                count[menu] = count.get(menu,0) + 1
        
        if count :
            max_count = max(count.values())
        
        if max_count >= 2 :
            for menu in count :
                if count[menu] == max_count :
                    answer.append(menu)
    return sorted(answer)