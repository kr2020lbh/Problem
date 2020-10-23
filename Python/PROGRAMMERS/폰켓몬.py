def solution(nums):

    set_length = len(set(nums))
    nums_length = len(nums)
    if set_length >= nums_length//2:
        return nums_length//2
    else:
        return set_length


print(solution([3,3,3,2,2,4]))