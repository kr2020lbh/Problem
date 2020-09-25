#정삼각형 분할 놀이
import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    a,b = map(int,input().split())
    print(f'#{t} {(a//b)**2}')
