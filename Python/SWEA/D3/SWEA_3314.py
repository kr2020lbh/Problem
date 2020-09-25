#보충학습과 평균
import sys
sys.stdin = open("input.txt","r")


for t in range(1,int(input())+1):
    print(f'#{t} {sum([i if i >= 40 else 40 for i in map(int,input().split()) ])//5}')
