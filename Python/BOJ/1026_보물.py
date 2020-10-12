import sys
sys.stdin = open("input.txt","r")
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort(reverse=True)
res = 0
for i in range(N):
    res += A[i]*B[i]
print(res)