a,b = map(int, input().split())

sort_list = list(map(int, input().split()))

sort_list.sort()

print(sort_list[b-1])