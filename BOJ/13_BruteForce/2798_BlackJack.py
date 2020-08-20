import sys
sys.stdin = open("input.txt","r")

N,M = map(int,input().split())
cards = list(map(int,input().split()))
blackjack = 0
result = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            blackjack = cards[i] + cards[j] + cards[k]
            if blackjack <= M and blackjack>result:
                result = blackjack
print(result)

