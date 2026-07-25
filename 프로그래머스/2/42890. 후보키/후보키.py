from itertools import combinations
def solution(relation):
    # 중복 안됨
    # 
    candidate_keys = []
    column_count = len(relation[0])
    
    # 선택한 컬럼 갯수 1개부터 전체 컬럼 수까지
    for size in range(1,column_count + 1) :
        
        for cols in combinations(range(column_count), size):
        
            is_minimal = True
        
            for key in candidate_keys :
                if set(key).issubset(set(cols)) :
                    is_minimal = False
                    break
            if not is_minimal :
                continue
            
            # 유일성 검사
            values = set()
        
            for row in relation :
                value = tuple(row[col] for col in cols)
                values.add(value)
            
            if len(values) == len(relation) :
                candidate_keys.append(cols)
            
    return len(candidate_keys)