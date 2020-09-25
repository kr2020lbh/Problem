#지그재그 숫자
import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    total = 0
    for i in range(1,int(input())+1):
        if i%2:
            total+=i
        else:
            total-=i
    print(f'#{t} {total}')

