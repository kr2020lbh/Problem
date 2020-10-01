import sys
sys.stdin = open("input.txt","r")
n,m = map(int,input().split())

print(n//m)
print(n%m)