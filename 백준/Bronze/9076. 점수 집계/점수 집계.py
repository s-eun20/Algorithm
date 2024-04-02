T = int(input())  # 테스트 케이스의 개수

for _ in range(T):
    scores = list(map(int, input().split()))  # 다섯 심판이 준 점수
    
    # 최고점과 최저점을 제외한 점수들을 구합니다.
    other_scores = sorted(scores)[1:4]
    
    # 최고점과 최저점의 차이가 4 이상인지 확인합니다.
    if other_scores[-1] - other_scores[0] >= 4:
        print("KIN")
    else:
        # 점수를 조정하지 않고 총점을 계산합니다.
        total_score = sum(other_scores)
        print(total_score)
