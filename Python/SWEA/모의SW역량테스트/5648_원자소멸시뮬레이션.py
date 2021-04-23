import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maps =[[0]*2001 for _ in range(2001)]
    print(maps)

