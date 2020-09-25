#쥬스 따르기
import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    N = int(input())
    print('#{}'.format(t),end=' ')
    for i in range(1,N+1):
        print('1/{}'.format(N),end=' ')
    print()

