import math
arr = [1,1,1,2,2,2,3,3,3,4,4,4]
N = len(arr)
cnt = 0
def perm(idx):
    global cnt
    if idx == N:
        print(cnt)
        cnt += 1
        return

    for i in range(idx, N):
        if i != idx and arr[i] == arr[idx]:
            continue
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]

# perm(0)
print(math.factorial(12)/6**4)
print(cnt)