import sys
sys.stdin = open("input.txt","r")

def is_palindrome(A,B):
    if A==B:return 1
    if B in palindrome[A]:return 1
    tmp_a = A
    tmp_b = B
    while tmp_a <= tmp_b:
        if NUMBERS[tmp_a] != NUMBERS[tmp_b]:return 0
        tmp_a += 1
        tmp_b -= 1
    while A <= B:
        palindrome[A].append(B)
        A += 1
        B -= 1
    return 1

N = int(input())
NUMBERS = list(map(int,input().split()))
M = int(input())
palindrome = [[] for _ in range(N)]
for _ in range(M):
    A,B = map(int,input().split())
    if is_palindrome(A-1,B-1):
        print(1)
    else:
        print(0)
