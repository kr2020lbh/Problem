import sys
sys.stdin = open("input.txt","r")

from itertools import combinations


def deliver_food(deliver_to,deliver_from,min_limit):
    SUM = 0
    used_delivery = set()
    for house in deliver_to:
        MIN = 10000
        r1 = house[0]
        c1 = house[1]

        for delivery in deliver_from:
            r2 = delivery[0]
            c2 = delivery[1]
            dist = abs(r1-r2)+abs(c1-c2)

            if dist < MIN:
                MIN = dist
                tmp_r2 = r2
                tmp_c2 = c2
        if (tmp_r2,tmp_c2) in used_delivery:
            SUM += MIN
        else:
            used_delivery.add((tmp_r2, tmp_c2))
            SUM += MIN + arr[tmp_r2][tmp_c2]


        if SUM > min_limit:
            return SUM
    return SUM

for t in range(1,int(input())+1):
    N = int(input())
    arr = []
    houses = []
    deliveries = []

    for row in range(N):
        arr.append(list(map(int,input().split())))
        for col in range(N):
            if arr[row][col] == 1:
                houses.append([row,col])
            if arr[row][col] >= 2:
                deliveries.append([row,col])

    MIN = 100000
    
    for i in range(1,len(deliveries)+1):
        for comb in combinations(deliveries,i):
            selected_deliveries = comb
            total = deliver_food(houses,selected_deliveries,MIN)
            if total < MIN:
                MIN = total

    print("#{} {}".format(t,MIN))

