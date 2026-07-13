def solution(s):
    stack = []

    for word in s:
        if stack and word == stack[-1]:
            stack.pop()
        else:
            stack.append(word)

    if not stack:
        return 1

    return 0