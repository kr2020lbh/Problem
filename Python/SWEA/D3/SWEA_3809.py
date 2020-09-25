import sys
sys.stdin = open("input.txt", "r")

for t in range(1,int(input())+1):
    N = int(input())
    result = ''
    while len(result)<N:
        result += input().replace(' ','')
    a=0
    while True:
        if str(a) not in result:
            break
        a+=1
    print(f'#{t} {a}')
