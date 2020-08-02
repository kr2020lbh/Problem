#직사각형 길이 찾기
import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    lengths = input().split()
    for length in lengths:
        if lengths.count(length) in [1,3]:
            print(f'#{t} {length}')
            break
