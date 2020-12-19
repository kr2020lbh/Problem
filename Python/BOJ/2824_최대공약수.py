import sys
sys.stdin = open("input.txt","r")

def gcd(a,b):
    if a > b:a,b = b,a
    while a:
        a,b = b%a, a
    b = str(b)
    if len(b) > 9:
        print(b[len(b)-9:len(b)])
    else:
        print(b)

N = int(input())
a = list(map(int,input().split()))
M = int(input())
b = list(map(int,input().split()))
A = B = 1
for _ in a:A*=_
for _ in b:B*=_
gcd(A,B)