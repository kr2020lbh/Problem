import sys
sys.stdin = open("input.txt","r")
N = int(input())
arr = list(map(int,input().split()))
res = []
for i in range(1,N+1):
    res.insert(len(res)-arr[i-1],i)
print(*res)