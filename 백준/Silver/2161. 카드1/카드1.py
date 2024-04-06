num = int(input())

card = [i for i in range(1, num+1)]
pop_card = []

while(len(card) != 1) :
  pop_card.append(card.pop(0))
  card.append(card.pop(0))



for i in pop_card :
  print(i, end=' ')
print(card[0])