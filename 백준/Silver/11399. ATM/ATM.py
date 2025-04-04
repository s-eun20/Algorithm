n = int(input())

people = list(map(int,input().split()))

people.sort()

total = 0
current_sum = 0

for i in range(n):
    current_sum += people[i]
    total +=current_sum
    
print(total)