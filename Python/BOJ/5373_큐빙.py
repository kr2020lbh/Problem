import sys
sys.stdin = open("input.txt","r")

T = int(input())
plane = {
    'U' : 0,
    'F' : 1,
    'D' : 2,
    'B' : 3,
    'L' : 4,
    'R' : 5
}
for _ in range(T):
    cube = [
        ['w']*9,
        ['r']*9,
        ['y']*9,
        ['o']*9,
        ['g']*9,
        ['b']*9
            ]

    UP = [3,5,1,4]
    FRONT = [0,5,2,4]
    LEFT = [0,1,2,3]

    N = int(input())
    actions = list(input().split())
    for action in actions:

        prev = None
        pivot = plane[action[0]]
        direction = action[1]

        if pivot == 0: # 위

            if direction == '+':
                for u in UP:
                    if prev == None:
                        prev = cube[u][0:3]
                    else:
                        now = cube[u][0:3]
                        cube[u][0:3] = prev
                        prev = now[::]
            else:
                for u in UP[::-1]:
                    if prev == None:
                        prev = cube[u][0:3]
                    else:
                        now = cube[u][0:3]
                        cube[u][0:3] = prev
                        prev = now[::]



        elif pivot == 1: # 정면


            if direction == '+':
                for f in FRONT:
                    if prev == None:
                        prev = cube[f][0:3]
                    else:
                        now = cube[f][0:3]
                        cube[f][0:3] = prev
                        prev = now[::]
            else:
                for f in FRONT[::-1]:
                    if prev == None:
                        prev = cube[f][0:3]
                    else:
                        now = cube[f][0:3]
                        cube[f][0:3] = prev
                        prev = now[::]

        elif pivot == 2: # 아래

            if direction == '+':
                pass
            else:
                pass

        elif pivot == 3: # 뒷면

            if direction == '+':
                pass
            else:
                pass

        elif pivot == 4: # 왼쪽

            if direction == '+':
                pass
            else:
                pass

        elif pivot == 5: # 오른쪽

            if direction == '+':
                pass
            else:
                pass

    print(cube)
