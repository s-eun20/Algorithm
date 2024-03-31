num_list = []
for _ in range(7) :
  number = int(input())
  if number%2!=0 :
    num_list.append(number)

if len(num_list) == 0 :
  print(-1)
else :
  print(sum(num_list))
  print(min(num_list))