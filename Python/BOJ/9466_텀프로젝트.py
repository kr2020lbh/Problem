import sys
sys.stdin = open("input.txt","r")


def solution(current):
    global answer
    while True:
        visited[current] = 1
        cycle.append(current)
        next = P[current]
        if visited[next]:
            if next in cycle:
                answer += len(cycle[cycle.index(next):])
            return
        else:
            current = next

for t in range(int(input())):
    N = int(input())
    P = list(map(int,input().split()))
    P = [0] + P
    visited = [1] + [0]*N
    answer = 0
    for i in range(1,N+1):
        if not visited[i]:
            cycle = []
            solution(i)
    print(N-answer)