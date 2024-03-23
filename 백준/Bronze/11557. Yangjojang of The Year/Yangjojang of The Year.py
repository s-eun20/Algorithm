T = int(input())


max_b = 0
name = ""

for _ in range(T) :
  N = int(input())
  for _ in range(N) :
    a,b = input().split()
    b=int(b)
    if b > max_b :
      max_b=b
      name=a
  print(name)