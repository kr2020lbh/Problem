import sys
sys.stdin = open("input.txt","r")
def f():
    MIN = 1000
    for i in range(N-1,-1,-1):
        if A[i] <= MIN and i not in res:
            MIN = A[i]
            idx = i
    res.append(idx)


N = int(input())
A = list(map(int,input().split()))
P = [-1]*N
res=[]
[f() for _ in range(N)]
for i in range(N):
    P[res[i]] = i
print(*P)
