import sys
sys.stdin = open("input.txt","r")
n = int(input())
directions = []
edges = []
for _ in range(6):
    direction, edge = map(int,input().split())
    directions.append(direction)
    edges.append(edge)
directions+=directions
edges+=edges
for i in range(9):
    if directions[i:i+4] == [3,1,3,1]:
        print((edges[i-1]*edges[i+4]-edges[i+1]*edges[i+2]) * n)
        break
    if directions[i:i+4] == [2,3,2,3]:
        print((edges[i-1]*edges[i+4]-edges[i+1]*edges[i+2]) * n)
        break
    if directions[i:i+4] == [4,2,4,2]:
        print((edges[i-1]*edges[i+4]-edges[i+1]*edges[i+2]) * n)
        break
    if directions[i:i+4] == [1,4,1,4]:
        print((edges[i-1]*edges[i+4]-edges[i+1]*edges[i+2]) * n)
        break
