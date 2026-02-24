import sys

N,M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
left = 0
sum_val = 0
count = 0

for right in range(N) :
    sum_val += A[right]
    
    while sum_val > M :
        sum_val -= A[left]
        left +=1
    if sum_val == M :
        count+=1

print(count)

