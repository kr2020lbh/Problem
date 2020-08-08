#쉬운 거스름돈
import sys
sys.stdin = open('input.txt','r')

bills = [50000,10000,5000,1000,500,100,50,10]
for t in range(1,int(input())+1):
    N = int(input())
    cnts = ''
    for bill in bills:
        cnt = N//bill
        N -= bill*cnt
        cnts += str(cnt)+' '

    print(f'#{t}\n{cnts}')