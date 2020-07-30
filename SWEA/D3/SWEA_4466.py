import sys
sys.stdin = open("input.txt", "r")
for t in range(1,int(input())+1):
    N,K = map(int,input().split())
    scores = list(map(int,input().split()))
    scores.sort(reverse=True)
    print(f'#{t} {sum(scores[:K])}')
