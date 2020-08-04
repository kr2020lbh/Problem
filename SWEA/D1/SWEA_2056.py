#연월일 달력
import sys
sys.stdin = open("input.txt","r")
months = list(range(1,13))
days = [31,28,31,30,31,30,31,31,30,31,30,31]
for t in range(1,int(input())+1):
    ymd = input()
    y,m,d = ymd[0:4],ymd[4:6],ymd[6:8]
    if int(d)<=days[int(m)-1] and int(m) in months:
        print(f'#{t} {y}/{m}/{d}')
    else:
        print(f'#{t} -1')

