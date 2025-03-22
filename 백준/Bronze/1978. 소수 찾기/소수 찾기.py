num = int(input())

a = list(map(int,input().split()))
prime_count = 0
for number in a :
  for i in range(2, number+1) :
    if number%i==0 :
      if number==i :
        prime_count+=1


      break

print(prime_count)
    