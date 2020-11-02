import sys
from itertools import permutations
import copy
sys.stdin = open("input.txt","r")
#
# def is_possible(index,arr,length,row,col):
#     if index == 0:
#         for i in range(row,row+length):
#             for j in range(col,col+length):
#                 if arr[i][j] == 0:
#                     return False
#
#         for i in range(row, row + length):
#             for j in range(col, col + length):
#                 arr[i][j] = 0
#         return True
#
#     if index == 1:
#         for i in range(row,row-length-1,-1):
#             for j in range(col,col+length):
#                 if arr[i][j] == 0:
#                     return False
#
#         for i in range(row,row-length-1,-1):
#             for j in range(col, col + length):
#                 arr[i][j] = 0
#         return True
#
#     if index == 2:
#         for i in range(row,row+length):
#             for j in range(col,col-length-1,-1):
#                 if arr[i][j] == 0:
#                     return False
#
#         for i in range(row, row + length):
#             for j in range(col,col-length-1,-1):
#                 arr[i][j] = 0
#         return True
#
#     if index == 3:
#         for i in range(row,row-length-1,-1):
#             for j in range(col,col-length-1,-1):
#                 if arr[i][j] == 0:
#                     return False
#
#         for i in range(row,row-length-1,-1):
#             for j in range(col,col-length-1,-1):
#                 arr[i][j] = 0
#         return True
#
# def solve(i,arr,length):
#     if i == 0:
#         for row in range(10-length+1):
#             for col in range(10-length+1):
#                 if is_possible(i,arr,length,row,col):
#                     res[i][length-1]+=1
#         if res[i][length - 1] > 5:
#             return False
#         return True
#
#     if i == 1:
#         for row in range(9,length-2,-1):
#             for col in range(10-length+1):
#                 print(row,col,length)
#                 if is_possible(i,arr,length,row,col):
#                     res[i][length-1]+=1
#         if res[i][length - 1] > 5:
#             return False
#         return True
#
#     if i == 2:
#         for row in range(10-length+1):
#             for col in range(9,length-2,-1):
#                 if is_possible(i,arr,length,row,col):
#                     res[i][length-1]+=1
#         if res[i][length - 1] > 5:
#             return False
#         return True
#
#     if i == 3:
#         for row in range(9,length-2,-1):
#             for col in range(9,length-2,-1):
#                 if is_possible(i,arr,length,row,col):
#                     res[i][length-1]+=1
#         if res[i][length - 1] > 5:
#             return False
#         return True
#
#
#
# arr = [list(map(int,input().split())) for _ in range(10)]
# ans = []
# for lengthes in permutations(range(1,6)):
#     res = [[0,0,0,0,0] for _ in range(4)]
#     for i in range(4):
#         tmp = copy.deepcopy(arr)
#         for length in lengthes:
#             if solve(i,tmp,length):
#                 continue
#             else:
#                 ans.append(-1)
#                 break
#         else:
#             ans.append(sum(res[i]))
#     print(res)
# MIN = 25
# if sum(ans)==-120:
#     print(-1)
# else:
#     for a in ans:
#         if a != -1:
#             if MIN > a:
#                 MIN = a
#     print(MIN)


def is_possible(row,col,n):
    if row+n>10 or col+n>10:
        return False
    for i in range(n):
        for j in range(n):
            if arr[row+i][col+j] == 0:
                return False
    return True


def dfs(depth,ones):
    global answer
    if depth >= answer:
        return
    if ones==0:
        answer = depth

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1:
                break
        if arr[i][j] == 1:
            break
    if arr[i][j] == 1:
        for n in range(1,6):
            if papers[n-1] > 0:
                if is_possible(i,j,n):
                    papers[n-1] -= 1
                    for d_i in range(n):
                        for d_j in range(n):
                            arr[i+d_i][j+d_j] = 0
                    dfs(depth+1,ones-n**2)
                    for d_i in range(n):
                        for d_j in range(n):
                            arr[i+d_i][j+d_j] = 1
                    papers[n-1] += 1

papers = [5,5,5,5,5]
arr = []
ones = 0
for _ in range(10):
    tmp = list(map(int,input().split()))
    ones+= tmp.count(1)
    arr.append(tmp)
answer = 26
dfs(0,ones)
if answer == 26:
    print(-1)
else:
    print(answer)