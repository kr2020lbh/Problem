import sys
sys.stdin = open("input.txt","r")

N = int(input())
nums = [[],[],[],[]]
for i in range(N):
    a,b,c,d = map(int,input().split())
    nums[0].append(a)
    nums[1].append(b)
    nums[2].append(c)
    nums[3].append(d)
for num in nums:
    num.sort()
sumation = 0
for a in range(N):
    sumation += nums[a]
    for b in range(N):
        for c in range(N):
            for d in range(N):
