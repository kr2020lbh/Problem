import sys
sys.stdin = open("input.txt","r")

from itertools import combinations

ans = 10**8
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
for comb in combinations(list(range(1,N)),N//2-1):
    team1 = [0] + list(comb)
    team2 = list(set(range(N))-set(team1))
    score1,score2 = 0,0
    for i in team1:
        for j in team1:
            score1 += arr[i][j]
    for i in team2:
        for j in team2:
            score2 += arr[i][j]
    ans = min(ans,abs(score1-score2))
print(ans)