import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    a,b = map(int,input().split())
    if a==b:
        ans = '='
    elif a>b:
        ans = '>'
    else:
        ans = '<'
    print(f'#{t} {ans}')