num = int(input())

for i in range(num) :
  a=int(input())
  b=int(input())
  floor = [j for j in range(1,b+1)]
  for l in range(a) :
    for m in range(1,b) :
      floor[m] +=floor[m-1]
  print(floor[b-1])