#간단한 압축 풀기
import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    count = 0
    print(f'#{t}')
    for i in range(N):
        for j in range(int(arr[i][1])):
            print(arr[i][0],end='')
            count +=1
            if count==10:
                count =0
                print()
                continue
    print()