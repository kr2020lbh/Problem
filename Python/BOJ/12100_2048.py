import sys
sys.stdin = open("input.txt","r")
#
# import copy
# def get_directions(depth,cur_dir):
#     if depth == 5:
#         directions.append(cur_dir)
#         return
#     for i in range(4):
#         get_directions(depth+1,cur_dir+[i])
#
# def move(maps,d):
#     if d == 0: #왼쪽으로 밀착
#         for row in range(N):
#             for col in range(N-1):
#                 me = maps[row][col]
#                 if me != 0:#내가 0이 아니고
#                     for k in range(col+1,N): #내 오른쪽이 0이면 계속 나아가고 나와 같다면
#                         you = maps[row][k]
#                         if you == 0: continue
#                         if you != me:break
#                         if you == me:
#                             maps[row][col] *= 2 #나는 2배 곱하고
#                             maps[row][k] = 0 #오른쪽은 0으로 만든다
#                             break
#             #row의 요소를 다 바꿨다면 이제 왼쪽으로 밀어야한다
#             zero_cnt = 0
#             new_row = []
#             for col in range(N):
#                 if maps[row][col] == 0:
#                     zero_cnt += 1
#                 else:
#                     new_row.append(maps[row][col])
#             new_row += [0]*zero_cnt
#             maps[row] = new_row
#
#     elif d == 1:#오른쪽으로 밀착
#         for row in range(N):
#             for col in range(N-1,0,-1):
#                 me = maps[row][col]
#                 if me != 0:#내가 0이 아니고
#                     for k in range(col-1,-1,-1): #내 왼쪽이 0이면 계속 나아가고 나와 같다면
#                         you = maps[row][k]
#                         if you == 0: continue
#                         if you != me:break
#                         if you == me:
#                             maps[row][col] *= 2 #나는 2배 곱하고
#                             maps[row][k] = 0 #왼쪽은 0으로 만든다
#                             break
#
#             #row의 요소를 다 바꿨다면 이제 오른쪽으로 밀어야한다
#             zero_cnt = 0
#             new_row = []
#             for col in range(N):
#                 if maps[row][col] == 0:
#                     zero_cnt += 1
#                 else:
#                     new_row.append(maps[row][col])
#             new_row = [0]*zero_cnt + new_row
#             maps[row] = new_row
#
#     elif d== 2: #위로 밀착
#         for col in range(N):
#             for row in range(N-1):
#                 me = maps[row][col]
#                 if me != 0:#내가 0이 아니고
#                     for k in range(row+1,N): #내 밑쪽이 0이면 계속 나아가고 나와 같다면
#                         you = maps[k][col]
#                         if you == 0: continue
#                         if you != me:break
#                         if you == me:
#                             maps[row][col] *= 2 #나는 2배 곱하고
#                             maps[k][col] = 0 #밑쪽은 0으로 만든다
#                             break
#
#             #col의 요소를 다 바꿨다면 이제 위쪽으로 밀어야한다
#             zero_cnt = 0
#             new_col = []
#             for row in range(N):
#                 if maps[row][col] == 0:
#                     zero_cnt += 1
#                 else:
#                     new_col.append(maps[row][col])
#             new_col += [0]*zero_cnt
#             for row in range(N):
#                 maps[row][col] = new_col[row]
#     else: #아래로 밀착
#         for col in range(N):
#             for row in range(N-1,0,-1):
#                 me = maps[row][col]
#                 if me != 0:#내가 0이 아니고
#                     for k in range(row-1,-1,-1): #내 위쪽이 0이면 계속 나아가고 나와 같다면
#                         you = maps[k][col]
#                         if you == 0: continue
#                         if you != me:break
#                         if you == me:
#                             maps[row][col] *= 2 #나는 2배 곱하고
#                             maps[k][col] = 0 #위쪽은 0으로 만든다
#                             break
#             #col의 요소를 다 바꿨다면 아래쪽으로 밀어야한다
#             zero_cnt = 0
#             new_col = []
#             for row in range(N):
#                 if maps[row][col] == 0:
#                     zero_cnt += 1
#                 else:
#                     new_col.append(maps[row][col])
#             new_col = [0]*zero_cnt + new_col
#             for row in range(N):
#                 maps[row][col] = new_col[row]
#     return maps
#
# N = int(input())
# maps = [list(map(int,input().split())) for _ in range(N)]
# directions = []
# get_directions(0,[])
# res = 0
#
# for direction in directions:
#     tmp_maps = copy.deepcopy(maps)
#
#     for d in direction:
#         tmp_maps = move(tmp_maps,d)
#
#     for i in range(N):
#         for j in range(N):
#             if res < tmp_maps[i][j]:
#                 res = tmp_maps[i][j]
# print(res)


tmp_maps = copy.deepcopy(maps)

for d in [3,3,1,2,3,0]:
    print('실행전')
    [print(t) for t in tmp_maps]
    print()
    tmp_maps = move(tmp_maps,d)
    if d == 0:
        print('왼쪽')
    if d == 1:
        print('오른쪽')
    if d == 2:
        print('위쪽')
    if d == 3:
        print('아래쪽')
    [print(t) for t in tmp_maps]
    print()


