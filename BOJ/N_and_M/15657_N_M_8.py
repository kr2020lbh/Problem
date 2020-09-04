import sys
sys.stdin = open("input.txt","r")
def f(idx,range_idx):
    if idx==M:
        print(' '.join(map(str,ptr)))
    else:
        for i in range(range_idx,N):
            ptr.append(arr[i])
            f(idx+1,i)
            ptr.pop()

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ptr = []
f(0,0)