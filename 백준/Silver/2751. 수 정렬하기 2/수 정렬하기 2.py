import sys

n = int(sys.stdin.readline())

lists = []

for _ in range(n):
    lists.append(int(sys.stdin.readline()))
    
    
lists = sorted(lists)
for i in lists:
    print(i)