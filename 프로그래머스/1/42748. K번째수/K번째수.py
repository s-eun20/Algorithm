def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        result = array[i-1:j]
        result = sorted(result)
        answer.append(result[k-1])
    
    return answer