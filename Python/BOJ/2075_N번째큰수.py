import sys
from queue import PriorityQueue
sys.stdin = open("input.txt","r")
N = int(input())
ans = []
for _ in range(int(input())):
    row = sorted(list(map(int,input().split())) + ans, reverse=True)
    ans = row[0:N]
print(ans[-1])
        