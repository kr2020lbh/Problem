def points(N, M,key, arr1, arr2, arr3, arr4):
    for i in range(0, N + M - 1):
        for j in range(0, N + M - 1):
            if check(i,j,N,key,arr1,arr2,arr3,arr4):
                return True
    else:
        return False


def check(i,j,N,key,arr1,arr2,arr3,arr4):
    cmp = [key[i+c][j:j+N] for c in range(N)]
    if cmp == arr1:
        return True
    if cmp == arr2:
        return True
    if cmp == arr3:
        return True
    if cmp == arr4:
        return True
    return False


def rotate_right(arr,N):
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = arr[N-1-j][i]
    return tmp


def rotate_left(arr,N):
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = arr[j][N-1-i]
    return tmp


def reverse_lock(arr,N):
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]==0:
                tmp[i][j]=1
    return tmp


def solution(key, lock):
    M = len(key)
    N = len(lock)
    new_key = [[0] * (2 * (N - 1) + M) for i in range(2 * (N - 1) + M)]
    for i in range(N - 1, N + M - 1):
        new_key[i][N - 1:N + M - 1] = key[i - (N - 1)]
    opposite_lock = reverse_lock(lock,N)
    lock_90 = rotate_left(opposite_lock,N)
    lock_180 = rotate_left(lock_90,N)
    lock_270 = rotate_right(opposite_lock,N)

    answer = points(N,M,new_key,opposite_lock,lock_90,lock_180,lock_270)
    return answer
