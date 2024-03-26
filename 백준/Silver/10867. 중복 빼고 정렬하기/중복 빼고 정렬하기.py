# 입력 받기
N = int(input())
numbers = list(map(int, input().split()))

# 중복 제거 및 정렬
sorted_numbers = sorted(set(numbers))

# 결과 출력
for num in sorted_numbers:
    print(num, end=" ")
