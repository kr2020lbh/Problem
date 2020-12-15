import sys
sys.stdin = open("input.txt","r")


def do_action(robot_idx,action,repeat):
    robot = robots[robot_idx]
    row,col = robot[0],robot[1]
    d = maps[row][col][1]
    if action == 'F':
        for i in range(repeat):
            d_row,d_col = row + delta[d][0], col + delta[d][1]
            if 0 <= d_row < B and 0<= d_col < A:
                if maps[d_row][d_col]:
                    crash = maps[d_row][d_col]
                    print("Robot {} crashes into robot {}".format(robot_idx + 1,crash[0]+1))
                    return False
                maps[row][col] = 0
                row = d_row
                col = d_col
                maps[row][col] = [robot_idx,d]

            else:
                print("Robot {} crashes into the wall".format(robot_idx+1))
                return False
        robots[robot_idx] = [row,col,d]
    if action == 'L':
        maps[row][col] = [robot_idx,(d-repeat)%4]
    if action == 'R':
        maps[row][col] = [robot_idx, (d+repeat)%4]
    return True

delta = [[-1,0],[0,1],[1,0],[0,-1]]
A,B = map(int,input().split())
N,M = map(int,input().split())
maps = [[0]*A for _ in range(B)]
robots = []; actions = []
for _ in range(N):
    loc = input().split()
    col = int(loc[0]) - 1
    row = B - (int(loc[1]) - 1) - 1
    if loc[-1] == 'N':
        d = 0
    elif loc[-1] == 'E':
        d = 1
    elif loc[-1] == 'S':
        d = 2
    else:
        d = 3
    robots.append([row,col,d])
    maps[row][col] = [_,d]

for _ in range(M):
    robot_idx, action, repeat = input().split()
    actions.append([int(robot_idx)-1,action,int(repeat)])
for robot_idx, action, repeat in actions:
    # [print(m) for m in maps]
    # print()
    if not do_action(robot_idx,action,repeat):
        break
else:
    print('OK')
