import sys
sys.stdin = open("input.txt","r")


def f(s,num):
    if s == 1:
        for i in range(num,n+1):
            if i % num == 0:
                switches[i-1] = male_switch(switches[i-1])
    if s == 2:
        female_switch(num)


def male_switch(num):
    if num == 0: return 1
    else: return 0


def female_switch(num):
    i = 1
    num-=1

    while num+i<n and num-i>=0 :
        if switches[num+i]!=switches[num-i]:
            break
        i+=1
    i -= 1

    for j in range(-i,i+1):
        if switches[num+j]==0: switches[num+j] = 1
        else: switches[num+j] = 0

n = int(input())
switches = list(map(int,input().split()))
student = [list(map(int,input().split())) for _ in range(int(input()))]

for command in student:

    s = command[0]
    num = command[1]
    f(s,num)

print_line = [20] *  (n//20)
print_line+= [n%20]
idx = 0
for i in range(len(print_line)):
    idx += print_line[i]
    for j in range(idx-print_line[i],idx):
        print(switches[j],end=' ')
    print()