def solution(dartResult):

    scores = []
    i = 0

    while i < len(dartResult):

        # 숫자 읽기 (10 처리)
        if dartResult[i].isdigit():
            if i + 1 < len(dartResult) and dartResult[i] == "1" and dartResult[i + 1] == "0":
                num = 10
                i += 1
            else:
                num = int(dartResult[i])

        elif dartResult[i] == "S":
            num = num ** 1
            scores.append(num)

        elif dartResult[i] == "D":
            num = num ** 2
            scores.append(num)

        elif dartResult[i] == "T":
            num = num ** 3
            scores.append(num)

        elif dartResult[i] == "*":
            scores[-1] *= 2
            if len(scores) >= 2:
                scores[-2] *= 2

        elif dartResult[i] == "#":
            scores[-1] *= -1

        i += 1

    return sum(scores)