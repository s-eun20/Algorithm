N=int(input())

str_list = []

for i in range(N):
    str_list.append(input())
    
    
str_list = sorted(set(str_list), key=lambda x: (len(x), x))  

# 출력
for word in str_list:
    print(word)