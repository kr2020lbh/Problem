import sys
sys.stdin = open("input.txt","r")


def f(idx,cursum):
    global MIN

    if cursum-B > MIN:
        return

    if idx == N:
        if cursum >= B:
            MIN = cursum-B
            return
    else:
        visited[idx]=1
        f(idx+1,cursum+heights[idx])
        visited[idx]=0
        f(idx+1,cursum)

for t in range(1,int(input())+1):
    N,B = map(int,input().split())
    heights = list(map(int,input().split()))
    MIN = N*B
    visited = [0]*N
    f(0,0)
    print("#{} {}".format(t,MIN))
