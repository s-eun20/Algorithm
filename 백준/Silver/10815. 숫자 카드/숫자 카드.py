n = int(input())

have = set(map(int, input().split()))

m = int(input())

test = list(map(int, input().split()))

result = []

for i in range(m) :
  if test[i] in have :
    result.append(1)
  else :
    result.append(0)

for i in result :
  print(i, end = ' ')