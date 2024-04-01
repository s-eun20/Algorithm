num = int(input())
sum=0
result=0
num_list = list(map(int, input().split()))
for i in range(num) :
  if num_list[i] == 1 :
    sum += 1
    result+=sum
  else :
    sum = 0


print(result)