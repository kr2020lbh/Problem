
def f(idx,range_idx):

    if idx==M:
        print(' '.join(map(str,ptr)))
    else:
        for i in range(range_idx,N):
            ptr.append(arr[i])
            f(idx+1,i)
            ptr.pop()

N,M = map(int,input().split())
arr = [i+1 for i in range(N)]
visited = [[0]*N for _ in range(M)]
ptr = []
f(0,0)
