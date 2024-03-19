def calculate_score(quiz_result):
    score = 0
    consecutive_O = 0

    for answer in quiz_result:
        if answer == 'O':
            consecutive_O += 1
            score += consecutive_O
        else:
            consecutive_O = 0

    return score

# 테스트 케이스 개수 입력
test_cases = int(input())

# 각 테스트 케이스에 대해 점수를 계산하고 출력
for _ in range(test_cases):
    quiz_result = input()
    print(calculate_score(quiz_result))
