import sys
sys.stdin = open("input.txt","r")

def memoization():
    for i in range(N): #길이 1
        palindrome[i][i] = 1
    for i in range(N - 1): #길이 2
        if NUMBERS[i] == NUMBERS[i + 1]:
            palindrome[i][i + 1] = 1
    for i in range(2, N): #길이 3 이상
        for j in range(N - i):
            if NUMBERS[j] == NUMBERS[j + i] and palindrome[j + 1][j + i - 1] == 1:
                palindrome[j][j + i] = 1

N = int(input())
NUMBERS = list(map(int,input().split()))
M = int(input())
palindrome = [[0]*N for _ in range(N)]
memoization()
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    if palindrome[a-1][b-1]:
        print(1)
    else:
        print(0)

