import sys
sys.stdin = open("input.txt","r")
N,K = map(int,input().split())
nums = [i for i in range(1,N+1)]
length = N
idx = K-1
result = []
while True:
    result.append(nums[idx])
    del nums[idx]

    idx -= 1
    length -= 1
    if length ==0:
        break
    idx+=K
    idx%=length
print('<',end='')
[print(a,end=', ') for a in result[:-1]]
print(result[-1],end='>')