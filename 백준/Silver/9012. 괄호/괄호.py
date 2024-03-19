def is_valid_parenthesis(parenthesis):
    stack = []

    for p in parenthesis:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return "NO"
            stack.pop()

    if not stack:
        return "YES"
    else:
        return "NO"

# 입력 받기
test_cases = int(input())

# 각 테스트 케이스에 대해 결과 출력
for _ in range(test_cases):
    parenthesis = input()
    print(is_valid_parenthesis(parenthesis))
