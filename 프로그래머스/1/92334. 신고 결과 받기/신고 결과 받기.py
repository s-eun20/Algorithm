def solution(id_list, report, k):
    # 1. 중복 신고 제거
    report = list(set(report))

    # 2. 신고당한 횟수 저장용 딕셔너리
    reported_count = {user: 0 for user in id_list}

    # 3. 각 유저가 누구를 신고했는지 저장
    report_by_user = {user: [] for user in id_list}

    for r in report:
        reporter, reported = r.split()
        reported_count[reported] += 1
        report_by_user[reporter].append(reported)

    # 4. 정지된 유저 리스트
    banned_users = [user for user, count in reported_count.items() if count >= k]

    # 5. 각 유저가 받은 메일 수 계산
    result = []
    for user in id_list:
        count = 0
        for reported in report_by_user[user]:
            if reported in banned_users:
                count += 1
        result.append(count)

    return result
