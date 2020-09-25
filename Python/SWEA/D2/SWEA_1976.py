#시각 덧셈
import sys
sys.stdin = open('input.txt','r')

for t in range(1,int(input())+1):
    h1,m1,h2,m2 = map(int,input().split())
    m = m1+m2
    h = h1+h2+m//60
    if h>12: h -=12
    print(f'#{t} {h} {m%60}')
