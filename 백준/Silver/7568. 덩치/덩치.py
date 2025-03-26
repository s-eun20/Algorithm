n = int(input())

sizes = []

for _ in range(n):
    a,b = map(int,input().split())
    sizes.append((a,b))

for i in sizes:
    rank = 1
    for j in sizes:
        if i[0] < j[0] and i[1]<j[1]:
            rank +=1
    print(rank,end=" ")