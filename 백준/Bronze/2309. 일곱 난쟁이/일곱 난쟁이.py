staure = []
for _ in range(9) :
  staure.append(int(input()))

staure.sort()

staure_sum = sum(staure)

for i in range(len(staure)) :
  for j in range(i+1,len(staure)) :
    if staure_sum - staure[i] - staure[j] == 100 :
      for k in range(len(staure)) :
        if k != i and k != j :
          print(staure[k])
        else :
          pass
      exit()
