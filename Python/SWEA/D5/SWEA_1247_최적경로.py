import sys
sys.stdin = open("input.txt", "r")
from itertools import permutations

# def get_distance(perm,home,company,visited):
#     global MIN,MIN_PERM
#     total = 0
#     prev_x,prev_y = company
#     for i in perm:
#         if MIN < total:return
#         cur_x,cur_y = locations[i][0:2]
#         total += abs(prev_x-cur_x) + abs(prev_y-cur_y)
#         prev_x,prev_y = cur_x,cur_y
#     home_x, home_y = home
#     total += abs(prev_x-home_x) + abs(prev_y-home_y)
#     if total < MIN:
#         MIN = total
#         MIN_PERM = perm
#     return

for t in range(1,int(input())+1):
    N = int(input())
    tmp = list(map(int,input().split()))
    locations = []
    for i in range(N+2):
        locations.append([tmp[i*2],tmp[i*2+1]])
    MIN = 999999999
    get_distance(0,0,0,0)
    print("#{} {}".format(t,MIN))


# for t in range(1,int(input())+1):
#     N = int(input())
#     tmp = list(map(int,input().split()))
#     locations = []
#     for i in range(N+2):
#         locations.append([tmp[i*2],tmp[i*2+1],(tmp[i*2]+tmp[i*2+1])/2])
#     company = locations[0][0:2]
#     home = locations[1][0:2]
#     MIN = 999999999
#     MIN_PERM = []
#     for perm in permutations(range(2,N+2),N):
#         get_distance(perm,home,company)
#     print("#{} {}".format(t,MIN))

# for t in range(1,int(input())+1):
#     N = int(input())
#     tmp = list(map(int,input().split()))
#     locations = []
#     for i in range(N+2):
#         locations.append([tmp[i*2],tmp[i*2+1]],)
#     company = locations[0]
#     home = locations[1]
#     MIN = 999999999
#     print(locations)
#     # print("#{} {}".format(t,MIN))