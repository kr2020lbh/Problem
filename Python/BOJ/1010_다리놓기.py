import sys
sys.stdin = open("input.txt","r")

def f(b,a):
    return fact(a)//(fact(a-b)*fact(b))

def fact(n):
    res = 1
    for i in range(1,n+1):
        res*=i
    return res

for t in range(int(input())):
    a,b = map(int,input().split())
    print(f(a,b))