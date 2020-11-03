import sys
sys.stdin = open("input.txt","r")
# N,M = map(int,input().split())
# nums = list(map(int,input().split()))
# num_sum = [0]*len(nums)
# num_sum[0] = nums[0]
#
# for i in range(1,len(nums)):
#     num_sum[i] = nums[i] + num_sum[i-1]
# num_sum = [0] + num_sum
#
# i = j = res = 0
#
# while i <= j:
#     while j < len(num_sum):
#         if num_sum[j] - num_sum[i] < M:j += 1
#         else:break
#     if j == len(num_sum):j -= 1
#     if num_sum[j] - num_sum[i] == M:res += 1
#     i += 1
#
# print(res)
n, m = map(int, input().split())
nums = list(map(int, input().split()))
i, sumation, res = 0, 0, 0

for num in nums:
    sumation += num
    while sumation > m:
        sumation -= nums[i]
        i += 1
    res += (sumation == m)

print(res)