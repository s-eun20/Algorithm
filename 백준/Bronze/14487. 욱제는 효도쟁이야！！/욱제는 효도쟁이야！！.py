num = int(input())

num_list = list(map(int, input().split()))

print(sum(num_list)-max(num_list))