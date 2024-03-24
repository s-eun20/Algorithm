alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

word = list(input())
result = []
count=0

for alpha in alp :
  if alpha in word :
    result.append(word.index(alpha))
  else :
    result.append(-1)


for i in range(len(result)) :
  print(result[i], end=" ")