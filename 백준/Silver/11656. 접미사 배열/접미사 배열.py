a = input()

a_list = []
result = []
for i in a:
  a_list.append(i)

for i in range(len(a_list)) :
  result.append(''.join(a_list[i:]))

result.sort()

for i in result:
  print(i)