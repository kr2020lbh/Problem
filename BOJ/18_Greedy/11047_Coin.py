import sys
sys.stdin = open("input.txt","r")

N,K = map(int,input().split())
coins = [ int(input()) for _ in range(N)]
result = 0
for coin in coins[::-1]:
    cnt = K//coin
    if cnt:
        K%=coin
    result+=cnt
print(result)



