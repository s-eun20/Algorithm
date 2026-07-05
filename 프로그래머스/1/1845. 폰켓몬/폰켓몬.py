def solution(nums):
    
    set_nums = set(nums)
    len_nums = len(set_nums)
    
    return min(len(nums)//2 , len_nums)


# 중복제거와 몇마리인지 중요ㅛ함
