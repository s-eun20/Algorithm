num1 = int(input())

num_list = []
for i in range(num1) :
  num_list = list(map(int, input().split()))
  avg = sum(num_list[1:]) / num_list[0]
  count=0
  for score in num_list[1:] :
    if score > avg :
      count +=1
  rate = count / num_list[0] * 100
  print(f'{rate:.3f}%')