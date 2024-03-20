num = []
for _ in range(28) :
  num.append(int(input()))


for number in range(1,31) :
  if number not in num :
    print(number)