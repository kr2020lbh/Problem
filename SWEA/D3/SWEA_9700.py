#USB 꽂기의 미스터리
import sys

sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    p,q = map(float,input().split())
    s1 = (1-p)*q
    s2 = p*(1-q)*q
    print(f'#{t} YES') if s1<s2 else print(f'#{t} NO')