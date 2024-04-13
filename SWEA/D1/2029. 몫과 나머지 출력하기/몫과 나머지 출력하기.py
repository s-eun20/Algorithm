num = int(input())

for i in range(1,num+1) :
  a,b = map(int,input().split())
  print("#"+str(i),int(a/b),int(a%b))