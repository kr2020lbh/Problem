#아름이의 돌 던지기 D2
import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    people = int(input())
    stones = list(map(int,input().split()))

    result = {}

    for stone in stones:
        stone=abs(stone)
        if result.get(stone):
            result[stone]+=1
        else:
            result[stone] = 1
    sorted_result = sorted(result)
    print(f'#{t} {sorted_result[0]} {result[sorted_result[0]]}')