#홍준이의 숫자 놀이
import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    A,B = map(int,input().split())

    if A%B==0:
        print(f'#{t} -1')
        break
    x=1
    y=(1-A*x)/B