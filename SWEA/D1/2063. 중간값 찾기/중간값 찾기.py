num = int(input())

num_list = list(map(int, input().split()))

num_list.sort()

print(num_list[num//2])