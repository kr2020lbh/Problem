import sys
sys.stdin = open("input.txt","r")

from itertools import permutations
def go(idx,N,perm,sumation):
    global MIN
    if sumation > MIN:
        return
    if idx == N:
        MIN = sumation
    else:
        if arr[perm[idx]][perm[idx+1]] != 0:
            go(idx+1,N,perm,sumation+arr[perm[idx]][perm[idx+1]])


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
MIN = 100000000
for perm in permutations(range(N),N):
    perm = list(perm)+[perm[0]]
    go(0,N,perm,0)
print(MIN)


