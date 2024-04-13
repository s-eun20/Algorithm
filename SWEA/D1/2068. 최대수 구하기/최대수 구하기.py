num = int(input())

for test_case in range(1,num+1) :
  max_num = map(int, input().split())
  print("#"+str(test_case)+" "+str(max(max_num)))