num = int(input())

a=[]

for _ in range(num) :
  w,h = map(int,input().split())
  a.append((w,h))

for i in a :
  rank = 1
  for j in a :
    if i[0] < j[0] and i[1] < j[1] :
      rank+=1
  print(rank,end=' ')