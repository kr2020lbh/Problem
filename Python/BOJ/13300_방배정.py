import sys
sys.stdin = open("input.txt","r")
N,K = map(int,input().split())
students = [[0]*6,[0]*6]

for i in range(N):
    S,Y = map(int,input().split())
    students[S][Y-1]+=1

res = 0
for student in students:
    for grade in student:
        share = grade//K
        remainder = grade%K
        if remainder==0:
            res+=share
        else:
            res+=(share+1)
print(res)