#1959 .두 개의 숫자열
import sys
sys.stdin = open("input.txt","r")
for t in range(1, int(input())+1):
    N,M = map(int,input().split())
    shorter = list(map(int, input().split()))
    longer = list(map(int, input().split()))
    if N>M:
        N, M = M, N
        shorter,longer =longer, shorter
    MAX = 0
    for k in range(M-N+1):
        multi = 0
        for i in range(N):
            multi+=shorter[i]*longer[k+i]
        if MAX < multi:
            MAX = multi
    print(f'#{t} {MAX}')
