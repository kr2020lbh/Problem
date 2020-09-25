#1961 .숫자 배열 회전
import sys
sys.stdin = open("input.txt","r")

def print_rot():
    end = N-1
    print(f'#{t}')
    for i in range(N):
        [print(arr[end-j][i],end='') for j in range(N)]
        print(end=' ')
        [print(arr[end-i][end-j], end='') for j in range(N)]
        print(end=' ')
        [print(arr[j][end-i], end='') for j in range(N)]
        print()

for t in range(1,int(input())+1):
    N = int(input())
    arr = [ list(map(int,input().split())) for _ in range(N) ]
    print_rot()
