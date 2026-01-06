def solution(array, commands):
    answer = []

    for i,j,k in commands:
        array2 = array[i-1:j]
        array2.sort()
        answer.append(array2[k-1])
            
    return answer