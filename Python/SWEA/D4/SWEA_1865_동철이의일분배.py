import sys
sys.stdin = open("input.txt","r")

def f(idx,cursum):
    global MAX

    if MAX >= cursum:
        return

    if idx == N-1:
        MAX = cursum

    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                f(idx+1,cursum*arr[idx+1][i]/100)
                visited[i] = 0



for t in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    MAX = 0
    for i in range(N):
        visited[i] = 1
        f(0,arr[0][i]/100)
        visited[i] = 0
    print("#{} {:6f}".format(t,round(MAX*100,6)))