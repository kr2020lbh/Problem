
def f(idx):

    if idx==M:
        print(' '.join(map(str,ptr)))
    else:
        for i in range(N):
            ptr.append(arr[i])
            f(idx+1)
            ptr.pop()

N,M = map(int,input().split())
arr = [i+1 for i in range(N)]
visited = [[0]*N for _ in range(M)]
ptr = []
f(0)
