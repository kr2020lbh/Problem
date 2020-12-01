import sys
import copy
sys.stdin = open("input.txt","r")
'''
CCTV
1번 -> 상, 우, 하, 좌 (4)
2번 -> 상하, 좌우 (2)
3번 -> 상, 우, 하, 좌 (4)
4번 -> 상, 우, 하, 좌 (4)
5번 -> 상하좌우 (1)
'''
def cctv_playing(cctv_numbers,cctv_location,office):
    global ans
    if sum(cctv_numbers) == 0:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if office[i][j] == 0:
                    cnt += 1
                    if cnt > ans:
                        return
        ans = cnt

    else:
        tmp_office = copy.deepcopy(office)
        cctv_num_idx,cctv_loc_idx = get_cctv(cctv_numbers,cctv_location)
        if cctv_num_idx == 1: #상하, 좌우
            for direction in range(2):
                cctv_playing_change_office(cctv_num_idx,cctv_location[cctv_num_idx][cctv_loc_idx],direction,tmp_office,1)
                cctv_numbers[cctv_num_idx] -= 1
                cctv_location[cctv_num_idx][cctv_loc_idx][-1] = True
                cctv_playing(cctv_numbers,cctv_location,tmp_office)
                cctv_numbers[cctv_num_idx] += 1
                cctv_location[cctv_num_idx][cctv_loc_idx][-1] = False
                cctv_playing_change_office(cctv_num_idx, cctv_location[cctv_num_idx][cctv_loc_idx], direction, tmp_office,-1)

        elif cctv_num_idx == 4: # 상하좌우
            cctv_playing_change_office(cctv_num_idx, cctv_location[cctv_num_idx][cctv_loc_idx], 0,tmp_office,1)
            cctv_numbers[cctv_num_idx] -= 1
            cctv_location[cctv_num_idx][cctv_loc_idx][-1] = True
            cctv_playing(cctv_numbers, cctv_location, tmp_office)
            cctv_numbers[cctv_num_idx] += 1
            cctv_location[cctv_num_idx][cctv_loc_idx][-1] = False
            cctv_playing_change_office(cctv_num_idx, cctv_location[cctv_num_idx][cctv_loc_idx], 0, tmp_office,-1)

        else:
            for direction in range(4): #상 우 하 좌
                cctv_playing_change_office(cctv_num_idx,cctv_location[cctv_num_idx][cctv_loc_idx],direction,tmp_office,1)
                cctv_numbers[cctv_num_idx] -= 1
                cctv_location[cctv_num_idx][cctv_loc_idx][-1] = True
                cctv_playing(cctv_numbers,cctv_location,tmp_office)
                cctv_numbers[cctv_num_idx] += 1
                cctv_location[cctv_num_idx][cctv_loc_idx][-1] = False
                cctv_playing_change_office(cctv_num_idx,cctv_location[cctv_num_idx][cctv_loc_idx],direction,tmp_office,-1)


def get_cctv(cctv_numbers,cctv_location):
    for i in range(len(cctv_numbers)):
        if cctv_numbers[i] != 0:
            for j in range(len(cctv_location[i])):
                if cctv_location[i][j][-1] == False:
                    return i,j


def cctv_playing_change_office(cctv_idx,cctv_loc,direction,office,change_number):
    cur_r, cur_c, visited = cctv_loc
    first_r, first_c = cur_r,cur_c
    if cctv_idx == 0: #상 우 하 좌
        while True:
            next_r = cur_r + d_r[direction]
            next_c = cur_c + d_c[direction]
            if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                return office
            elif office[next_r][next_c] == 6:
                return office
            else:
                office[next_r][next_c] += change_number
                cur_r,cur_c = next_r,next_c

    elif cctv_idx == 1: #상하,좌우
        if direction == 0: #상하
            while True:
                next_r = cur_r + d_r[direction]
                next_c = cur_c + d_c[direction]
                if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                    break
                elif office[next_r][next_c] == 6:
                    break
                else:
                    office[next_r][next_c] += change_number
                    cur_r, cur_c = next_r, next_c

            cur_r,cur_c = first_r,first_c
            while True:
                next_r = cur_r + d_r[direction+2]
                next_c = cur_c + d_c[direction+2]
                if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                    return office
                elif office[next_r][next_c] == 6:
                    return office
                else:
                    office[next_r][next_c] += change_number
                    cur_r, cur_c = next_r, next_c
        else: #좌우
            while True:
                next_r = cur_r + d_r[direction]
                next_c = cur_c + d_c[direction]
                if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                    break
                elif office[next_r][next_c] == 6:
                    break
                else:
                    office[next_r][next_c] += change_number
                    cur_r, cur_c = next_r, next_c

            cur_r,cur_c = first_r,first_c
            while True:
                next_r = cur_r + d_r[direction+2]
                next_c = cur_c + d_c[direction+2]
                if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                    return office
                elif office[next_r][next_c] == 6:
                    return office
                else:
                    office[next_r][next_c] += change_number
                    cur_r, cur_c = next_r, next_c
    elif cctv_idx == 2:#상 우 하 좌
        while True:
            next_r = cur_r + d_r[direction]
            next_c = cur_c + d_c[direction]
            if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                break
            elif office[next_r][next_c] == 6:
                break
            else:
                office[next_r][next_c] += change_number
                cur_r, cur_c = next_r, next_c

        cur_r,cur_c = first_r,first_c
        while True:
            next_r = cur_r + d_r[(direction+1)%4]
            next_c = cur_c + d_c[(direction+1)%4]
            if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                return office
            elif office[next_r][next_c] == 6:
                return office
            else:
                office[next_r][next_c] += change_number
                cur_r, cur_c = next_r, next_c

    elif cctv_idx == 3:#상 우 하 좌
        while True:
            next_r = cur_r + d_r[direction]
            next_c = cur_c + d_c[direction]
            if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                break
            elif office[next_r][next_c] == 6:
                break
            else:
                office[next_r][next_c] += change_number
                cur_r, cur_c = next_r, next_c

        cur_r,cur_c = first_r,first_c
        while True:
            next_r = cur_r + d_r[(direction+1)%4]
            next_c = cur_c + d_c[(direction+1)%4]
            if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                break
            elif office[next_r][next_c] == 6:
                break
            else:
                office[next_r][next_c] += change_number
                cur_r, cur_c = next_r, next_c

        cur_r,cur_c = first_r,first_c
        while True:
            next_r = cur_r + d_r[(direction-1)%4]
            next_c = cur_c + d_c[(direction-1)%4]
            if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                return office
            elif office[next_r][next_c] == 6:
                return office
            else:
                office[next_r][next_c] += change_number
                cur_r, cur_c = next_r, next_c
    elif cctv_idx == 4:#상하좌우
        while True:
            next_r = cur_r + d_r[0]
            next_c = cur_c + d_c[0]
            if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                break
            elif office[next_r][next_c] == 6:
                break
            else:
                office[next_r][next_c] += change_number
                cur_r, cur_c = next_r, next_c

        cur_r, cur_c = first_r, first_c
        while True:
            next_r = cur_r + d_r[1]
            next_c = cur_c + d_c[1]
            if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                break
            elif office[next_r][next_c] == 6:
                break
            else:
                office[next_r][next_c] += change_number
                cur_r, cur_c = next_r, next_c

        cur_r, cur_c = first_r, first_c
        while True:
            next_r = cur_r + d_r[2]
            next_c = cur_c + d_c[2]
            if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                break
            elif office[next_r][next_c] == 6:
                break
            else:
                office[next_r][next_c] += change_number
                cur_r, cur_c = next_r, next_c

        cur_r, cur_c = first_r, first_c
        while True:
            next_r = cur_r + d_r[3]
            next_c = cur_c + d_c[3]
            if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                return office
            elif office[next_r][next_c] == 6:
                return office
            else:
                office[next_r][next_c] += change_number
                cur_r, cur_c = next_r, next_c

N,M = map(int,input().split())
office = []
ans = 64
cctv_location = [[] for _ in range(5)]
cctv_numbers = [0,0,0,0,0]
d_r = [-1,0,1,0]
d_c = [0,1,0,-1]
for i in range(N):
    row = list(map(int,input().split()))
    office.append(row)
    for j in range(M):
        if row[j] == 1:
            cctv_location[0].append([i,j,False])
            cctv_numbers[0] += 1
        elif row[j] == 2:
            cctv_location[1].append([i,j,False])
            cctv_numbers[1] += 1
        elif row[j] == 3:
            cctv_location[2].append([i,j,False])
            cctv_numbers[2] += 1
        elif row[j] == 4:
            cctv_location[3].append([i,j,False])
            cctv_numbers[3] += 1
        elif row[j] == 5:
            cctv_location[4].append([i,j,False])
            cctv_numbers[4] += 1
cctv_playing(cctv_numbers,cctv_location,office)
print(ans)