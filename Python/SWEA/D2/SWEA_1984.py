#중간 평균값 구하기
import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    num = sorted(list(map(int,input().split())))[1:9]
    print(f'#{t} {round(sum(num)/len(num))}')