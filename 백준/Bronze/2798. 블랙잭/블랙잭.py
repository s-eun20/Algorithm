from itertools import combinations

N,M =map(int,input().split())

cards = list(map(int, input().split()))

com_cards = combinations(cards,3)

sum = 0

for i,j,k in com_cards :
    if i+j+k >sum and i+j+k <= M :
        sum = i+j+k        
        
print(sum)