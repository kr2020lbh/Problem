import sys
sys.stdin = open("input.txt","r")
#1번 연산은 상하 반전
#2번 연산은 좌우 반전
#3번 연산은 오른쪽 90도
#4번 연산은 왼쪽 90도
#5번 연산은 4개의 부분으로 나누고 좌상부분으로 우상으로, 우상으로 우하 우하를 좌하 좌하를 좌상으로
#6번 연산은 5번의 반대로 돌린다.
def command1(arr):
    new_arr = []
    for row in arr[::-1]:
        new_arr.append(row)
    return new_arr


def command2(arr):
    new_arr = []
    for row in arr:
        new_arr.append(row[::-1])
    return new_arr


def command3(arr):
    return list(map(list,zip(*arr[::-1])))


def command4(arr):
    for i in range(3):
        arr = command3(arr)
    return arr


def command5(arr):
    new_arr = []
    first = []
    second = []
    third = []
    forth = []

    N = len(arr)
    M = len(arr[0])

    for i in range(N//2):
        first.append(arr[i][0:M//2])
        second.append(arr[i][M//2:M])

    for i in range(N//2,N):
        third.append(arr[i][M//2:M])
        forth.append(arr[i][0:M//2])

    for i in range(N//2):
        new_arr.append(forth[i]+first[i])
    for i in range(N//2):
        new_arr.append(third[i]+second[i])

    return new_arr


def command6(arr):
    new_arr = []
    first = []
    second = []
    third = []
    forth = []

    N = len(arr)
    M = len(arr[0])

    for i in range(N // 2):
        first.append(arr[i][0:M // 2])
        second.append(arr[i][M // 2:M])

    for i in range(N // 2, N):
        third.append(arr[i][M // 2:M])
        forth.append(arr[i][0:M // 2])

    for i in range(N // 2):
        new_arr.append(second[i] + third[i])
    for i in range(N // 2):
        new_arr.append(first[i] + forth[i])

    return new_arr


N,M,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
commands = list(map(int,input().split()))
for command in commands:
    if command==1:
        arr = command1(arr)
    elif command==2:
        arr = command2(arr)
    elif command==3:
        arr = command3(arr)
    elif command==4:
        arr = command4(arr)
    elif command==5:
        arr = command5(arr)
    else:
        arr = command6(arr)

[print(*a) for a in arr]

