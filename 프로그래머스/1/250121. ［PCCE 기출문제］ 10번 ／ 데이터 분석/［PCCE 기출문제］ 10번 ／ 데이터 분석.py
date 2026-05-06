def solution(data, ext, val_ext, sort_by):
    result = []

    # 각 항목 이름과 인덱스 매핑
    idx = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }

    # 조건 필터링
    for item in data:
        if item[idx[ext]] < val_ext:
            result.append(item)

    # 정렬
    result.sort(key=lambda x: x[idx[sort_by]])

    return result