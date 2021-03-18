import sys
sys.stdin = open("input.txt","r")


ans =10000000000
ap,al,ar = 0,1,2
N = int(input())
nums = sorted(list(map(int,input().split())))
for i in range(N-2):
    l,r = i+1,N-1
    while l < r:
        tmp = nums[i]+nums[l]+nums[r]
        if abs(tmp) < ans:
            ap,al,ar = i,l,r
            ans = abs(tmp)
        if ans == 0:
            break
        if tmp < 0:
            l += 1
        else:
            r -= 1
print(*[nums[ap],nums[al],nums[ar]])