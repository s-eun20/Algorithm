import sys
n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(list(map(int, sys.stdin.readline().split())))
num.sort(key=lambda x: (x[0], x[1]))
for i in num:
    print(i[0], i[1])