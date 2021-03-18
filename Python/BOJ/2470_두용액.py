import sys
sys.stdin = open("input.txt","r")


N = int(input())
nums = sorted(list(map(int,input().split())))
l,r = 0,N-1
al,ar = l,r
ans = nums[l] + nums[r]
while l < r:
    tmp = nums[l] + nums[r]

    if abs(tmp) < abs(ans):
        ans = tmp
        al,ar = l,r
    if tmp == 0:
        break
    if tmp > 0:
        r -= 1
    else:
        l += 1
print(nums[al],nums[ar])
