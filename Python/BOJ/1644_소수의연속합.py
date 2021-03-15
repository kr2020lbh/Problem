import sys
sys.stdin = open("input.txt","r")
N = int(input())
nums = []

mat = [0 for i in range(N+1)]
mat[0] = 1
mat[1] = 1
for i in range(2,N+1):
    if mat[i]==0:
        for j in range(i,N+1,i):
            mat[j] = 1
        nums.append(i)

if nums:
    left,right,ans = 0,0,0
    sumation = nums[left]

    while left < len(nums):
        if sumation == N:
            ans += 1
            sumation -= nums[left]
            left += 1
        elif sumation < N:
            right += 1
            if right < len(nums):
                sumation += nums[right]
            else:
                break
        else:
            sumation -= nums[left]
            left += 1
    print(ans)
else:
    print(0)


