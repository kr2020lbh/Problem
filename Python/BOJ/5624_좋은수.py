import sys
sys.stdin = open("input.txt","r")

N = int(input())
A = list(map(int,input().split()))
NUM = 200000
nums = [0] * 400001
ans = 0
for i in range(N):
    for j in range(i):
        if nums[A[i]-A[j]+NUM]:
            ans += 1
            break
    for j in range(i+1):
        nums[A[i]+A[j]+NUM] = 1

print(ans)
