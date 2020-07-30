import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    numbers = list(map(int,input().split()))
    print(f'#{t} {sum([number for number in numbers if number%2])}')