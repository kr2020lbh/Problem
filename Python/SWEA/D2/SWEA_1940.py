#가랏! RC카!
import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    N=int(input())
    commands=[ list(map(int,input().split())) for _ in range(N)]
    vel = distance = 0

    for command in commands:
        if command[0]==1:
            vel+=command[1]
        elif command[0]==2:
            if command[1] > vel:
                vel = 0
            else:
                vel-=command[1]
        distance+=vel

    print(f'#{t} {distance}')