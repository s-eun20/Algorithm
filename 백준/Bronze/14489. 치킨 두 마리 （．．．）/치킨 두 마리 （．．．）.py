a,b = map(int, input().split())
price = int(input())

if a+b >= 2*price :
    print(a+b - (2*price))
else :
    print(a+b)