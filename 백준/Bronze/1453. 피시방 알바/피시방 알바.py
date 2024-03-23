pc =[]
count = 0
for i in range(101) :
  pc.append(i+1)

num = int(input())

people = list(map(int, input().split()))

for i in range(num) :
  if people[i] in pc :
    pc.remove(people[i])
  else :
    count+=1

print(count)