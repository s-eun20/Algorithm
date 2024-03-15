number = int(input())

changes = 1000-number

coins =(500,100,50,10,5,1)
count = 0

for coin in coins :
  count +=changes//coin
  changes%=coin

print(count)