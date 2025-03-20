from collections import Counter

N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
num2_list = list(map(int, input().split()))

counter = Counter(num_list)  # num_list에서 숫자의 개수를 미리 세기
result = [counter[num] for num in num2_list]  # num2_list에 있는 숫자의 개수 찾기

print(*result)