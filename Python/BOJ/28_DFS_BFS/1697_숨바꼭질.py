import sys
sys.stdin = open("input.txt","r")
from collections import deque

def bfs():
    ans=0
    while Q:
        k = Q.popleft()
        tmp = []
        for num in k:
            if num==N:
                return ans
            if num%2==1:
                if num>=0 and visited[num-1]==0:
                    visited[num-1]=1
                    tmp.append(num-1)
                if visited[num+1]==0:
                    visited[num+1]=1
                    tmp.append(num+1)
            else:
                if visited[num//2]==0:
                    visited[num//2]=1
                    tmp.append(num // 2)
                if num>=0 and visited[num-1]==0:
                    visited[num-1]=1
                    tmp.append(num-1)
                    tmp.append(num-1)
                if visited[num+1]==0:
                    visited[num+1]=1
                    tmp.append(num+1)
        Q.append(tmp)
        ans+=1
    return ans

visited = [0] * 100100
N,K = map(int,input().split())
if K<=N:print(N-K)
else:
    Q = deque()
    Q.append([K])
    print(bfs())

