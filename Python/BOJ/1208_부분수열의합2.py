import sys
sys.stdin = open("input.txt","r")
N,S = map(int,input().split())
nums = sorted(list(map(int,input().split())))
print(nums)
left,right,ans = 0,0,0
sumation = nums[left]
while left < len(nums):
    if sumation == S:
        sumation -= nums[left]
        left += 1
        ans += 1
    elif sumation < S:
        right += 1
        if right < len(nums):
            break
        sumation += nums[right]
    else:
        sumation -= nums[left]
        left += 1
print(ans)

