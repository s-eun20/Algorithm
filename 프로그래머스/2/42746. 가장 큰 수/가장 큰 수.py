def repeat(x):
    return x * 3


def solution(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(key=repeat, reverse=True)

    answer = ''.join(numbers)

    if answer[0] == '0':
        return '0'

    return answer