#2806. N-Queen
# 길이 N의 col 배열은 각각이 인덱스가 열을 나타내고
# 그 안의 요소가 행을 나타낸다. 즉 col[0]=3 이면 3행 1열에 queen이 있는 것
# queen의 위치를 1차원 배열로 나타낸다!!
# queen 함수를 통해서 col[X] = i -->  0열  0~N-1 행에 첫 번째 queen을 두고
# 그 다음 어떻게 되는지 본다
# possible_queen 함수를 통해서 그 자리에 둘 수 있는지, 있다면 다음 열로 넘어가는 방식
# col[X]==col[i] 을 통해 같은 행에 존재하는지 확인
# abs(col[X]-col[i])==X-i 을 통해 대각선에 존재하는지 확인
import sys
sys.stdin = open("input.txt","r")

def queen(X):
    global count
    global N

    if X == N:
        count+=1
    else:
        for i in range(N):
            col[X]=i
            if possible_queen(X):
                queen(X+1)

def possible_queen(X):
    for i in range(X):
        if col[X]==col[i] or abs(col[X]-col[i])==X-i:
            return False
    else:
        return True

for t in range(1,int(input())+1):
    N = int(input())
    col = [0] * N
    count = 0
    queen(0)
    print(f'#{t} {count}')
