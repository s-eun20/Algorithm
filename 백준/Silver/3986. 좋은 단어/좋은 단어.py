num = int(input())

count = 0
for i in range(num) :
  stack = []
  word = list(input())
  for i in word :
    if not len(stack) :
      stack.append(i)
    elif stack[-1] == i :
      stack.pop(-1)
    else :
      stack.append(i)

  if not len(stack) :
    count+=1

print(count)