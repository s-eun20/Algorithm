N = int(input())

count = 1
room = 1

while room < N :
  room+=6*count
  count+=1

print(count)