def split_file(file):
    head = ''
    number = ''
    i = 0

    # 1. HEAD 추출 (숫자가 나오기 전까지)
    while i < len(file) and not file[i].isdigit():
        head += file[i]
        i += 1

    # 2. NUMBER 추출 (최대 5자리 숫자)
    while i < len(file) and file[i].isdigit() and len(number) < 5:
        number += file[i]
        i += 1

    return head, number

def solution(files):
    return sorted(files, key=lambda x: (
        split_file(x)[0].lower(),  
        int(split_file(x)[1])      
    ))
