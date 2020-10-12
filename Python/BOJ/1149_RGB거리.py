import sys
sys.stdin = open("input.txt","r")

N = int(input())
prices = []
for i in range(N):
    prices.append(list(map(int,input().split())))

for i in range(1,N):
    prices[i][0] = min(prices[i-1][1],prices[i-1][2]) + prices[i][0]
    prices[i][1] = min(prices[i-1][0],prices[i-1][2]) + prices[i][1]
    prices[i][2] = min(prices[i-1][0],prices[i-1][1]) + prices[i][2]
print(min(prices[-1]))