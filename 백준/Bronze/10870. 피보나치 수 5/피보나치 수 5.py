F=[]

for i in range(21) :
  if i >=2:
    F.append(F[i-2]+F[i-1])
  else :
    F.append(i)

num = int(input())
print(F[num])