import sys
sys.stdin = open("input.txt","r")
N = int(input())
details = [ list(map(int,input().split())) for _ in range(N)]
result = []
for detail in details:
    count = 1
    for compare in details:
        if detail[0]<compare[0] and detail[1]<compare[1]:
            count += 1
    print(count,end=' ')