import sys
sys.stdin = open('input.txt','r')

def dfs(n,k,m):
    global MIN

    if m-B>MIN:
        return

    if n == k:
        result = 0
        for i in range(n):
            if A[i]==1:
                result+=H[i]
        tmp = result-B
        if tmp>=0 and MIN > tmp:
            MIN = tmp

    else:
        A[k] = 1
        dfs(n,k+1,m+H[k])
        A[k] = 0
        dfs(n,k+1,m)


for t in range(1,int(input())+1):
    N,B = map(int,input().split())
    H = list(map(int,input().split()))
    A = [0] * N
    MIN = 10000
    dfs(N,0,0)

    print('#{} {}'.format(t,MIN))