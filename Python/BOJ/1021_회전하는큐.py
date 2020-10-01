import sys
sys.stdin = open("input.txt","r")


def left_move(left,right,target,length):
    cnt = 0

    while True:
        if Q[left] == target:
            return [cnt,left,right]
        left=(left+1)%length
        right=(right+1)%length
        cnt+=1


def right_move(left,right,target,length):
    cnt = 0

    while True:
        if Q[left] == target:
            return [cnt,left,right]
        left-=1
        right-=1
        if left < 0:
            left = length-1
        if right < 0:
            right = length-1
        cnt+=1


N,M = map(int,input().split())
targets = list(map(int,input().split()))
Q = list(range(1,N+1))
length = N
left = 0
right = N-1
ans = 0

for target in targets:
    if length == 1:
        continue
    l_move = left_move(left,right,target,length)
    r_move = right_move(left,right,target,length)


    if l_move[0] <= r_move[0]:
        ans += l_move[0]
        Q.pop(l_move[1])
        if l_move[1]<l_move[2]:
            right = l_move[2]-1
            left = l_move[1]
        else:
            if l_move[1] == length-1:
                right = r_move[2]-1
                left = 0
            else:
                right = r_move[2]
                left = l_move[1]

    else:
        ans += r_move[0]
        Q.pop(r_move[1])
        if r_move[1]<r_move[2]:
            right = r_move[2]-1
            left = r_move[1]
        else:
            if r_move[1] == length-1:
                right = r_move[2]-1
                left = 0
            else:
                right = r_move[2]
                left = r_move[1]

    length-=1

print(ans)



