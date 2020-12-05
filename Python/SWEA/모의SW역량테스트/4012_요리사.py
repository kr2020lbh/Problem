import sys
sys.stdin = open("input.txt","r")
from itertools import combinations as comb
for t in range(1,int(input())+1):
    N = int(input())
    S = [list(map(int,input().split())) for _ in range(N)]
    res = 50000
    idx = [i for i in range(N)]
    for c in comb(range(N),N//2):
        A = list(set(idx) - set(c))
        B = list(set(c))
        S_A = S_B = 0
        for i in range(N//2):
            for j in range(N//2):
                if j != i:
                    S_A += S[A[i]][A[j]]
                    S_B += S[B[i]][B[j]]
        tmp = abs(S_A - S_B)
        if res > tmp:
            res = tmp
    print("#{} {}".format(t,res))

