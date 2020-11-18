import sys
sys.stdin = open("input.txt","r")

def matrix_multiplication(A,B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    elif B%2 == 1:
        new_A = [[0]*N for _ in range(N)]
        C = matrix_multiplication(A,B-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    new_A[i][j] += A[i][k] * C[k][j]
                new_A[i][j] %= 1000
        return new_A
    else:
        new_A = [[0]*N for _ in range(N)]
        C = matrix_multiplication(A,B//2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    new_A[i][j] += C[i][k] * C[k][j]
                new_A[i][j] %= 1000
        return new_A

N,B=map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
[print(*matrix) for matrix in matrix_multiplication(A,B)]