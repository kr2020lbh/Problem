#날짜 계산기
import sys
sys.stdin = open("input.txt","r")

days = [31,28,31,30,31,30,31,31,30,31,30,31]
for t in range(1, int(input())+1):
    m1,d1,m2,d2 = map(int,input().split())
    print(f'#{t} {sum(days[m1-1:m2-1])-d1+d2+1}')