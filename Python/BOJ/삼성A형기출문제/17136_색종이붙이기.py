import sys
from itertools import permutations
import copy
sys.stdin = open("input.txt","r")

def is_possible(index,arr,length,row,col):
    if index == 0:
        for i in range(row,row+length):
            for j in range(col,col+length):
                if arr[i][j] == 0:
                    return False

        for i in range(row, row + length):
            for j in range(col, col + length):
                arr[i][j] = 0
        return True

    if index == 1:
        for i in range(row,row-length-1,-1):
            for j in range(col,col+length):
                if arr[i][j] == 0:
                    return False

        for i in range(row,row-length-1,-1):
            for j in range(col, col + length):
                arr[i][j] = 0
        return True

    if index == 2:
        for i in range(row,row+length):
            for j in range(col,col-length-1,-1):
                if arr[i][j] == 0:
                    return False

        for i in range(row, row + length):
            for j in range(col,col-length-1,-1):
                arr[i][j] = 0
        return True

    if index == 3:
        for i in range(row,row-length-1,-1):
            for j in range(col,col-length-1,-1):
                if arr[i][j] == 0:
                    return False

        for i in range(row,row-length-1,-1):
            for j in range(col,col-length-1,-1):
                arr[i][j] = 0
        return True

def solve(i,arr,length):
    if i == 0:
        for row in range(10-length+1):
            for col in range(10-length+1):
                if is_possible(i,arr,length,row,col):
                    res[i][length-1]+=1
        if res[i][length - 1] > 5:
            return False
        return True

    if i == 1:
        for row in range(9,length-2,-1):
            for col in range(10-length+1):
                print(row,col,length)
                if is_possible(i,arr,length,row,col):
                    res[i][length-1]+=1
        if res[i][length - 1] > 5:
            return False
        return True

    if i == 2:
        for row in range(10-length+1):
            for col in range(9,length-2,-1):
                if is_possible(i,arr,length,row,col):
                    res[i][length-1]+=1
        if res[i][length - 1] > 5:
            return False
        return True

    if i == 3:
        for row in range(9,length-2,-1):
            for col in range(9,length-2,-1):
                if is_possible(i,arr,length,row,col):
                    res[i][length-1]+=1
        if res[i][length - 1] > 5:
            return False
        return True



arr = [list(map(int,input().split())) for _ in range(10)]
ans = []
for lengthes in permutations(range(1,6)):
    res = [[0,0,0,0,0] for _ in range(4)]
    for i in range(4):
        tmp = copy.deepcopy(arr)
        for length in lengthes:
            if solve(i,tmp,length):
                continue
            else:
                ans.append(-1)
                break
        else:
            ans.append(sum(res[i]))
    print(res)
MIN = 25
if sum(ans)==-120:
    print(-1)
else:
    for a in ans:
        if a != -1:
            if MIN > a:
                MIN = a
    print(MIN)
