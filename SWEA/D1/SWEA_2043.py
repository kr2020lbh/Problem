#서랍의 비밀번호
import sys
sys.stdin = open("input.txt","r")

P,K = map(int,input().split())
ans = 1
while P!=K:
    ans+=1
    K=(K+1)%1000
print(ans)