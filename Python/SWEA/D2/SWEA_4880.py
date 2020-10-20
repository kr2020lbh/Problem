# 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임
import sys
sys.stdin = open("input.txt","r")


def winner(x,y):
    if (games[x-1] == 1 and games[y-1] == 3) or (games[x-1] == 1 and games[y-1] == 1):
        return x
    if (games[x-1] == 2 and games[y-1] == 1) or (games[x-1] == 2 and games[y-1] == 2):
        return x
    if (games[x-1] == 3 and games[y-1] == 2) or (games[x-1] == 3 and games[y-1] == 3):
        return x
    return y


def divide(first,last):
    if first == last:
        return first

    l = divide(first, (first+last)//2)
    r = divide((first+last)//2+1, last)
    return winner(l,r)

for t in range(1,int(input())+1):
    N = int(input())
    games = list(map(int,input().split()))
    print("#{} {}".format(t, divide(1,N)))


