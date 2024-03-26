# 입력 받기
N = int(input())

for _ in range(N) :
  numbers = list(map(int, input().split()))
  numbers.sort(reverse=True)
  print(numbers[2])