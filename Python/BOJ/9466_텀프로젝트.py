import sys
sys.stdin = open("input.txt","r")


for t in range(int(input())):
    N = int(input())
    P = list(map(int,input().split()))
    P = [0] + P
    print(P)
