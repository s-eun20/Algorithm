def solution(a, b, c):
    count = len({a, b, c})

    if count == 3:
        return a + b + c
    elif count == 2:
        return (a + b + c) * (a*a + b*b + c*c)
    else:
        return (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)