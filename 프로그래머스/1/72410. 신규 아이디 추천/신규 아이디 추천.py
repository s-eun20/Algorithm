def solution(new_id):
    # 1. 대문자 -> 소문자
    new_id = new_id.lower()
    # 2. 소문자,숫자,-,_,. 를 제외한 모든 문자 삭제
    answer = ""

    for ch in new_id:
        if ch.islower() or ch.isdigit() or ch in "-_.":
            answer += ch

    new_id = answer
    # 3. 마침표 두 개 연속은 하나로 치환
    while ".." in new_id :
        new_id = new_id.replace("..",".")
    # 4. 마침표 처음이나 끝은 제거
    new_id = new_id.strip(".")
    # 5. 만약 빈문자열이면 a 대입
    if new_id == "" :
        new_id = "a"
    # 6. 길이가 16자 이상 -> 15개 뒤에는 다 제거
    if len(new_id) >= 16 :
        new_id = new_id[:15]
        new_id = new_id.rstrip(".")
    # 7. 2자 이하면 마지막 문자를 반복 최대 세번?
    while len(new_id) < 3 :
        new_id += new_id[-1]
    
    return new_id