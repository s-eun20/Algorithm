# 함수 정의: 거스름돈 계산
def calculate_change(cents):
    quarters = cents // 25
    cents %= 25
    
    dimes = cents // 10
    cents %= 10
    
    nickels = cents // 5
    cents %= 5
    
    pennies = cents
    
    return quarters, dimes, nickels, pennies

# 테스트 케이스 수 입력
T = int(input())

# 각 테스트 케이스에 대해 거스름돈 계산 및 출력
for _ in range(T):
    C = int(input())  # 거스름돈 입력
    result = calculate_change(C)  # 거스름돈 계산
    print(*result)  # 결과 출력
