import sys
sys.stdin = open("input.txt","r")
N = int(input())
tri = []
for _ in range(N):
    tri.append(list(map(int,input().split())))
for n in range(N-2,-1,-1):
    for k in range(n+1):
        tri[n][k] += max(tri[n+1][k],tri[n+1][k+1])
print(tri[0][0])