import sys
sys.stdin = open("input.txt","r")
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    num = int(sys.stdin.readline())
    arr.append(num)
arr.sort()
for i in range(N):
    print(arr[i])