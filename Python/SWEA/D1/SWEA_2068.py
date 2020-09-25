#최대수 구하기
import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    print(f'#{t} {max(list(map(int, input().split())))}')
