def solution(priorities, location):
    # 1) (우선순위, 원래 인덱스) 형태로 큐 만들기
    queue = [(p, i) for i, p in enumerate(priorities)]
    
    printed = 0  # 출력된 문서 개수(=순서)

    while queue:
        # 2) 맨 앞 문서 꺼내기
        cur_p, cur_i = queue.pop(0)

        # 3) 지금 큐 안에 cur_p 보다 더 큰 우선순위가 있는지 확인
        if any(cur_p < p for p, _ in queue):
            # 더 큰 게 있으면 뒤로 보냄
            queue.append((cur_p, cur_i))
        else:
            # 4) 없으면 출력 처리
            printed += 1
            if cur_i == location:
                return printed
