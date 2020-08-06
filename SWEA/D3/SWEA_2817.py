#2817. 부분 수열의 합
import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    N,K = map(int,input().split())
    mylist = list(map(int,input().split()))
    count = 0
    for i in range(1<<N):
        tmp = []
        for j in range(N):
            if i & (1<<j):
                tmp.append(mylist[j])
        if sum(tmp)==K:
            count+=1
    print(f'#{t} {count}')
