#1244. [S/W 문제해결 응용] 2일차 - 최대 상금
import sys
sys.stdin = open("input.txt","r")


def make_change(nums):
    for i in range(len(nums)-1):
        if nums[i] >= max(nums[i+1::]):
            continue
        else:
            MAX = 0
            for j in range(i+1,len(nums)):
                if nums[j] >= MAX:
                    MAX = nums[j]
                    idx = j
            nums[i],nums[idx] = nums[idx], nums[i]
            return nums
    else:
        nums[len(nums)-1],nums[len(nums)-2] = nums[len(nums)-2],nums[len(nums)-1]
        return nums

def make_smaller():
    pass


for t in range(1,int(input())+1):
    nums, N = map(int,input().split())
    nums = list(map(int, str(nums)))
    max_nums = sorted(nums,reverse=True)
    print(nums,max_nums,N)

    for i in range(N):
        nums = make_change(nums)
    print()


