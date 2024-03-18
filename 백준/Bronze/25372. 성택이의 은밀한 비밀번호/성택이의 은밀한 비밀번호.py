num = int(input())

for _i in range(num) :
  pwd = input()
  if 6 <= len(pwd) <= 9:
    print("yes")
  else :
    print("no")