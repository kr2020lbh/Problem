import sys
sys.stdin = open("input.txt", "r")
from itertools import permutations
for t in range(1,int(input())+1):
    N = int(input())
    MIN = 10000
    path = [list(map(int,(input().split()))) for _ in range(N)]
    for perm in permutations(range(1,N),N-1):
        battery = 0
        order = [0] + list(perm) + [0]
        for i in range(N):
            if battery > MIN:
                break
            battery += path[order[i]][order[i+1]]
        if battery < MIN:
            MIN = battery
    print("#{} {}".format(t,MIN))


