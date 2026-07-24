from math import gcd
from functools import reduce
def solution(arrayA, arrayB):
    # 철수와 영희가 가진 각각의 카드의 최대공약수를 구해야함
    # reduce 함수는 리스트를 처음부터 끝까지 돌면서 이전 계산 결과와 다음 원소를 계속 계산해 주는 함수
    gcdA = reduce(gcd,arrayA)
    gcdB = reduce(gcd,arrayB)
    
    answer = 0
    vaild = True
    for number in arrayB :
        if number % gcdA == 0 :
            vaild = False
            break
            
    if vaild :
        answer = gcdA
    vaild2 = True
    for number in arrayA :
        if number % gcdB == 0 :
            vaild2 = False
            break
    if vaild2 :
        answer = max(gcdA,gcdB)
            
    return answer