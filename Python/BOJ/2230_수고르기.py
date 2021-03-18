import sys
sys.stdin = open("input.txt","r")
N,M = map(int,input().split())
nums =sorted([int(input()) for _ in range(N)])
l,r = 0,0
ans = 10000000000
while True:
    if l == N or r == N:
        break
    tmp = nums[r] - nums[l]
    if tmp == M:
        ans = tmp
        break
    elif tmp < M:
        r += 1
    else:
        if tmp < ans:
            ans = tmp
        l += 1
print(ans)

