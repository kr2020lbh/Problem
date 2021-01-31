import sys
from copy import deepcopy
sys.stdin = open("input.txt", "r")


def eat_fish(arr, i, j):
    index = []
    d = arr[i][j][1] - 1
    while True:
        d_i, d_j = i+delta[d][0], j+delta[d][1]
        if 0 <= d_i < 4 and 0 <= d_j < 4:
            if 1 <= arr[d_i][d_j][0] <= 16:
                index.append([d_i, d_j])
            i, j = d_i, d_j
        else:
            break

    return index


def find_fish(number, arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == number:
                return [i, j]
    else:
        return False


def move_fish(arr, shark_i, shark_j):
    for fish_number in range(1, 17):
        isExist = find_fish(fish_number, arr)
        if isExist:
            i, j = isExist
            d = arr[i][j][1] - 1
            # 해당방향으로 물고기 이동이 가능한지 확인
            step = 0
            while step < 8:
                d_i = i + delta[d][0]
                d_j = j + delta[d][1]
                if 0 <= d_i < 4 and 0 <= d_j < 4:
                    if not(d_i == shark_i and d_j == shark_j):
                        # 자리 바꾸기
                        arr[i][j][0], arr[d_i][d_j][0] = arr[d_i][d_j][0], arr[i][j][0]
                        arr[i][j][1], arr[d_i][d_j][1] = arr[d_i][d_j][1], d+1
                        break
                d = (d+1) % 8
                step += 1


def dfs(arr, i, j, eat_status):
    global answer
    arr = deepcopy(arr)
    fish_number = arr[i][j][0]
    arr[i][j][0] = -1
    move_fish(arr, i, j)
    result = eat_fish(arr, i, j)
    answer = max(answer, eat_status+fish_number)
    for d_i, d_j in result:
        dfs(arr, d_i, d_j, eat_status+fish_number)


delta = {
    0: [-1, 0],
    1: [-1, -1],
    2: [0, -1],
    3: [1, -1],
    4: [1, 0],
    5: [1, 1],
    6: [0, 1],
    7: [-1, 1],
}
maps = []
for i in range(4):
    maps.append([])
    row = list(map(int, input().split()))
    for j in range(4):
        maps[i].append([row[2*j], row[2*j+1]])

answer = 0
dfs(maps, 0, 0, 0)
print(answer)
