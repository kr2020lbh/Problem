import sys
sys.stdin = open("input.txt","r")

def checkEmpty(r,c):
    emptyCnt = 0
    for dr,dc in around:
        nr,nc = r+dr,c+dc
        if 0<= nr < N and 0<= nc < N:
            if maps[nr][nc] == 0:
                emptyCnt+=1
    return emptyCnt

def checkFav(r,c,nums):
    favCnt = 0
    for dr,dc in around:
        nr,nc = r+dr,c+dc
        if 0<= nr < N and 0<= nc < N:
            if maps[nr][nc] in nums:
                favCnt+=1
    return favCnt

scores = [0,1,10,100,1000]
around = [[-1,0],[0,1],[1,0],[0,-1]]
N = int(input())
maps = [[0]*N for _ in range(N)]
students = {}
for _ in range(N**2):
    nums = list(map(int,input().split()))
    students[nums[0]] = nums[1:]
    arr = []
    for i in range(N):
        for j in range(N):
            if maps[i][j]:
                continue
            tmpFavCnt = checkFav(i,j,nums)
            tmpEmptyCnt = checkEmpty(i,j)
            arr.append([tmpFavCnt,tmpEmptyCnt,i,j])
    arr.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    maps[arr[0][2]][arr[0][3]] = nums[0]

ans = 0
for i in range(N):
    for j in range(N):
        nums = students[maps[i][j]]
        ans += scores[checkFav(i,j,nums)]
print(ans)