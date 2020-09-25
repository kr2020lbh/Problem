import sys
sys.stdin = open("input.txt","r")
#실행시간 초과
# for t in range(1,int(input())+1):
#     A,B,C,D = map(int,input().split())
#     if (A/B)>(C/D):
#         ans = 'ALICE'
#     elif (A/B)<(C/D):
#         ans = 'BOB'
#     else:
#         ans = 'DRAW'
#     print(f'#{t} {ans}')
mylist = []
result = []
T=int(input())
for t in range(1,T+1):
    mylist.append(list(map(int,input().split())))
for t in range(T):
    alice = mylist[t][0]/mylist[t][1]
    bob = mylist[t][2]/mylist[t][3]
    if alice>bob:
        ans = 'ALICE'
    elif alice<bob:
        ans = 'BOB'
    else:
        ans = 'DRAW'
    result.append(f'#{t+1} {ans}')
print('\n'.join(result))
    