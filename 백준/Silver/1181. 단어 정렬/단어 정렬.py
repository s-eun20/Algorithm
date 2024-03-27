n=int(input())

eng=[]
for i in range(n) :
    eng.append(input())
    
set_eng=set(eng)
eng=list(set_eng)
eng.sort()
eng.sort(key=len)

for i in eng :
    print(i)