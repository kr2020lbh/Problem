import sys
sys.stdin = open("input.txt","r")
def f(idx,range_idx):
    if idx==M:
        print(' '.join(map(str,ptr)))


    else:
        for i in range(range_idx,N):
            if visited[i]== 1:
                continue

            visited[i]=1
            ptr.append(arr[i])
            f(idx+1,i+1)
            visited[i]=0
            ptr.pop()

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [0]*N
ptr = []
f(0,0)