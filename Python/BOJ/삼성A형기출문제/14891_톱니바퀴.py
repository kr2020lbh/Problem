import sys
sys.stdin = open("input.txt","r")

def check_left(gear_num,direction):
    moves = []
    pivot_gear = gears[gear_num][6]
    for i in range(gear_num-1,-1,-1):
        cmp_gear = gears[i][2]
        if cmp_gear != pivot_gear: #움직인다.
            moves.append([i,direction*-1])
            direction *= -1
            pivot_gear = gears[i][6]
        else:
            break
    return moves


def check_right(gear_num,direction):
    moves = []
    pivot_gear = gears[gear_num][2]
    for i in range(gear_num+1,4):
        cmp_gear = gears[i][6]
        if cmp_gear != pivot_gear: #움직인다.
            moves.append([i,direction*-1])
            direction *= -1
            pivot_gear = gears[i][2]
        else:
            break
    return moves


def rot(direction,gear_num):
    gear = gears[gear_num]
    if direction==1: #시계방향
        tmp = [gear[-1]] + gear[0:len(gear)-1]
    else: #반시계방향
        tmp = gear[1::] + [gear[0]]
    gears[gear_num] = tmp[::]


gears = [list(map(int,input())) for _ in range(4)]
K = int(input())
for _ in range(K):
    gear_num,d = map(int,input().split())
    gear_num -= 1
    tmp = [[gear_num,d]]
    if gear_num == 0:#첫번째 기어
        tmp+=check_right(gear_num,d)
    elif gear_num == 3:#마지막 기어
        tmp+=check_left(gear_num,d)
    else: #중간 위치 기어
        tmp+= check_left(gear_num,d) + check_right(gear_num,d)

    for gn,d in tmp:
        rot(d,gn)
ans = 0
for i in range(4):
    if gears[i][0] == 1:
        ans += 2**i 
print(ans)