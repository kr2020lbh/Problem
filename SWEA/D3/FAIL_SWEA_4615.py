import sys
import pprint
sys.stdin = open("input.txt", "r")
for t in range(1,int(input())+1):
    black = 0
    white = 0
    N,M = map(int,input().split())
    osello = [[(x+1,y+1) for x in range(N)] for y in range(N)]
    osello[N//2-1][N//2-1] = 2 #white
    osello[N//2][N//2] = 2 #white
    osello[N//2-1][N//2] = 1 #black
    osello[N//2][N//2-1] = 1 #black
    for _ in range(M):
        x,y,stone = map(int,input().split())
        osello[y-1][x-1] = stone
    for line in osello:
        black += line.count(1)
        white += line.count(2) 
    print(osello)
    print(black,white)
        
# check horizon -> 
    # left = until index 0
    # right = until index N-1
# check veritcal -> 
    # up = until index 0
    # down = until index N-1
# check diagonal -> 
    # leftup = x,y 가 둘 중 하나 0
    # leftdown = x,y 가 둘 중 하나 
    # rightup
    # rightdown



# osello = [[0 for x in range(6)] for y in range(6)]
# osello[6//2-1][6//2-1] = 'W'
# osello[6//2][6//2] = 'W'
# osello[6//2-1][6//2] = 'B'
# osello[6//2][6//2-1] = 'B'
# pprint.pprint(osello)
