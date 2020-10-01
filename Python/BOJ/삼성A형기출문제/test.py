import sys
from itertools import permutations
import copy
sys.stdin = open("input.txt","r")

def dfs(arr,row,col,paper):
    if row + paper < 10 and col + paper < 10:
        if is_possible(arr,row,col,paper) and used_paper[paper-1]<5:
            used_paper[paper-1]+=1
            for p in papers:
                for i in range(10):
                    for j in range(10):
                        if i + paper < 10 and j + paper < 10:
                            dfs(changed_arr(arr,row,col,paper),i,j,p)


def changed_arr(arr,row,col,paper):
    tmp = copy.deepcopy(arr)
    for i in range(row,row+paper):
        for j in range(col,col+paper):
            tmp[i][j] = 0
    return tmp


def is_possible(arr,row,col,paper):
    for i in range(row,row+paper):
        for j in range(col,col+paper):
            if arr[i][j]==0:
                return False
    else: return True


ans = []
papers = [5,4,3,2,1]
arr = [list(map(int,input().split())) for _ in range(10)]
for paper in papers:
    for i in range(10):
        for j in range(10):
            used_paper=[0]*5
            dfs(arr,i,j,paper)
            print(used_paper)