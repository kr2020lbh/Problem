#퍼펙트 셔플
import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    N = int(input())
    cards = list(input().split())
    first, second = cards[:(N+1)//2],cards[(N+1)//2:]
    result =''
    i=0
    if N%2:
        while(i<N//2):
            result+=first[i:i+1][0]+' '+second[i:i+1][0]+' '
            i+=1
        result+=first[-1]
    else:
        while(i<N//2):
            result+=first[i:i+1][0]+' '+second[i:i+1][0]+' '
            i+=1

    print(f'#{t} {result}')

