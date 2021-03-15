import sys
sys.stdin = open("input.txt","r")
N,M = map(int,input().split())
nums = list(map(int,input().split()))
left,right = 0,0
ans,sumation = 0,nums[left]
while left < N:
    if sumation == M:
        sumation -= nums[left]
        left +=1 
        ans += 1
    elif sumation < M:
        right += 1
        if right == N:
            break
        sumation += nums[right]
    else:
        sumation -= nums[left]
        left += 1
print(ans)