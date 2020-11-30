import sys
from itertools import combinations
sys.stdin = open("input.txt","r")

def get_chicken_distance(chicken,MIN_DIST):
    distance = 0
    for hX,hY in homes:
        distance += get_closest_chicken(hX,hY,chicken)
        if MIN_DIST < distance:
            return MIN_DIST
    return distance


def get_closest_chicken(hX,hY,chicken):
    min_dist=50000
    for cX,cY in chicken:
        tmp_dist = abs(hX-cX) + abs(hY-cY)
        if min_dist > tmp_dist:
            min_dist = tmp_dist
    return min_dist


N,M = map(int,input().split())
homes = []
chickens = []
MIN_DIST = 5000000
for i in range(N):
    row = list(map(int,input().split()))
    for j in range(N):
        if row[j] == 1:
            homes.append([i,j])
        elif row[j] == 2:
            chickens.append([i,j])

for chicken in combinations(chickens,M):
    MIN_DIST = get_chicken_distance(chicken,MIN_DIST)
print(MIN_DIST)
