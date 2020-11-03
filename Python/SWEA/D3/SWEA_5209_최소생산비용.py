import sys
sys.stdin = open("input.txt", "r")

def dfs(total,depth,flag):
    global MIN
    if MIN < total:
        return
    if depth == N:
        MIN = total
    else:
        for i in range(N):
            if not(flag & 1<<i):
                dfs(total+costs[depth][i],depth+1,flag | 1<<i)


for t in range(1,int(input())+1):
    N = int(input())
    costs = [list(map(int,input().split())) for _ in range(N)]
    MIN = 1500
    visited = [0] * N
    dfs(0,0,0)
    print("#{} {}".format(t,MIN))
