num = int(input())

for test_case in range(1,num+1) :
  a,b = map(int, input().split())
  if a>b :
    print('#'+str(test_case),">")
  elif a<b :
    print('#'+str(test_case),"<")
  else :
    print('#'+str(test_case),"=")