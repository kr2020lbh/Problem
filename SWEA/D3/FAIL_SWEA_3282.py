#0/1 Knapsack
import sys
sys.stdin = open("input.txt","r")

for t in range(1, int(input())+1):
    N,k = map(int,input().split())
    tmp = [0]*N
    for i in range(N):
        vclist = list(map(int,input().split()))
        vclist.append(vclist[1]/vclist[0])
    print(sorted(tmp,key = lambda x: x[0][-1]))
