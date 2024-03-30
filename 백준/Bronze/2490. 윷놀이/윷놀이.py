
count  = []
for _ in range(3) :
  a,b,c,d = map(int,input().split())
  count.append((a,b,c,d))

for i in range(3) :
  if count[i].count(1) == 4 :
    print("E")
  elif count[i].count(1) == 3 :
    print("A")
  elif count[i].count(1) == 2 :
    print("B")
  elif count[i].count(1) == 1 :
    print("C")
  else :
    print("D")