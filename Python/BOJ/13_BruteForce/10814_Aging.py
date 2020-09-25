import sys
sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    arr.append([i,age,name])
arr.sort(key=lambda x:((int(x[1])),x[0]))
for i in range(N):
    print(arr[i][1],arr[i][2])