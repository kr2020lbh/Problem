#영준이와 신비한 뿔의 숲
import sys
sys.stdin = open("input.txt","r")

for T in range(1,int(input())+1):
    n,m = map(int,input().split())
    t = m
    u = 0
    while 2*t+u !=n:
        u+=1
        t-=1
    print(f'#{T} {u} {t}')