import sys
sys.stdin = open("input.txt","r")

def findGroup():
    pass

def gravity():
    pass

def rot():
    pass

around = [[-1,0],[0,1],[1,0],[0,-1]]

N,M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
print(maps)