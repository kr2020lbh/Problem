N = int(input())
cord = []
for i in range(N):
    cord.append(list(map(int,input().split())))
cord.sort(key=lambda x:(x[0],x[1]))
for xy in cord:
    print(xy[0],xy[1])