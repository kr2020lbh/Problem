import sys
sys.stdin = open("input.txt","r")
N,M = map(int,input().split())
nums = list(map(int,input().split()))
num_sum = [0]*len(nums)
num_sum[0] = nums[0]
res = 0

for i in range(1,len(nums)):
    num_sum[i] = nums[i] + num_sum[i-1]
num_sum = [0] + num_sum
print(num_sum)
if M in num_sum:
    res += 1
for i in range(1,len(num_sum)):
    for j in range(i+1,len(num_sum)):
        if num_sum[j] - num_sum[i-1] == M:
            res += 1
            break

        if num_sum[j] - num_sum[i-1] > M:
            break
print(res)