from itertools import combinations
def solution(number):
    threes = list(combinations(number,3))
    count = 0
    for three in threes :
        if sum(three) == 0 :
            count += 1
            
    return count
        