import sys
sys.stdin = open("input.txt","r")


for t in range(1, int(input())+1):
    col = int(input())
    stickers = [list(map(int,input().split())) for _ in range(2)]
    stickers[0][1] += stickers[1][0]
    stickers[1][1] += stickers[0][0]
    for i in range(2,col):
        stickers[0][i] += max(stickers[1][i-1],stickers[1][i-2])
        stickers[1][i] += max(stickers[0][i-1],stickers[0][i-2])
    print(max(stickers[0][col-1],stickers[1][col-1]))


