#그래프의 삼각형
import sys
sys.stdin = open("input.txt", "r")

for t in range(1,int(input())+1):
    N,M= map(int,input().split())

    nodes = [[0]*N for _ in range(N)]
    for i in range(M):
        x,y = map(int,input().split())
        nodes[x-1][y-1]=1
        nodes[y-1][x-1]=1
    count = 0
    for i in range(N):
        node = nodes[i][i+1:N]
        for j in range(len(node)-1):
            for k in range(j+1,len(node)):
                if node[j]==1 and node[k]==1 and nodes[i+1+j][i+1+k]==1:
                    count+=1
    print(f'#{t} {count}')