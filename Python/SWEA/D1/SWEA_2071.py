import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    print(f'#{t} {round(sum(list(map(int,input().split())))/10)}')