#[S/W 문제해결 기본] 1일차 - 최빈수 구하기 D2
import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    T = int(input())
    numbers = list(map(int,input().split()))

    result = [0]*101
    max_count = 0

    for number in numbers:
        result[number]+=1
    for idx,counts in enumerate(result):
        if max_count <= counts:
            max_count = counts
            max_number = idx

    print(f'#{T} {max_number}')

