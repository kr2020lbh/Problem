import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    N=int(input())
    scores = list(map(int,input().split()))
    dp = [0]*(sum(scores)+1)
    dp[0]=1
    for score in scores:
        for i in range(len(dp)-1,-1,-1):
            if dp[i] == 1:
                dp[i+score] = 1
    print("#{} {}".format(t,sum(dp)))