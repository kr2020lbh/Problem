import sys
sys.stdin = open("input.txt","r")
N = int(sys.stdin.readline())
cord = []
for i in range(N):
    cord.append(list(map(int,sys.stdin.readline().split())))
cord.sort(key=lambda x:(x[1],x[0]))
for xy in cord:
    print(xy[0],xy[1])