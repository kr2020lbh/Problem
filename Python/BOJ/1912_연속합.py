import sys
sys.stdin = open("input.txt","r")
N = int(input())
nums = list(map(int,input().split()))
sumations = [nums[0]]
for i in range(N-1):
    sumations.append(max(sumations[i]+nums[i+1],nums[i+1]))
print(max(sumations))