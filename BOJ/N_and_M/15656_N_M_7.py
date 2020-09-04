import sys
sys.stdin = open("input.txt","r")
def f(idx):
    if idx==M:
        print(' '.join(map(str,ptr)))
    else:
        for i in range(N):
            ptr.append(arr[i])
            f(idx+1)
            ptr.pop()

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [0]*N
ptr = []
f(0)