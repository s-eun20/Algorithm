def solution(nums):
    
    set_data = set(nums)
    list_data = list(set_data)
    
    return min(len(list_data), len(nums) // 2)