char_len = int(input())

char = input()

list_char = list(char)

hash_sum = 0
power = 1

MOD = 1234567891
BASE = 31  

for i in range(char_len) :
    sum = (ord(list_char[i]) - ord('a')+1)
    
    hash_sum = (hash_sum + sum * power) % MOD
    
    power = (power * BASE) % MOD
    
print(hash_sum)
    