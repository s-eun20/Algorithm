def solution(arr):
    stack = []
    for x in arr:
        if not stack or stack[-1] != x:
            stack.append(x)
    return stack