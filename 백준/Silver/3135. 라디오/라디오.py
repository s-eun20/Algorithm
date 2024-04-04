A,B = map(int,input().split())
num  = int(input())
radio = abs(A-B)
for _ in range(num) :
  number = int(input())
  if radio > abs(number-B) :
    radio = abs(number-B)+1

print(radio)