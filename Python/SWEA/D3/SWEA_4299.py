import sys
sys.stdin = open("input.txt", "r")

for t in range(1,int(input())+1):
    D,H,M = map(int,input().split())
    D_rest = D-11
    H_rest = H-11
    M_rest = M-11

    if((D_rest == 0 and H_rest<0) or (D_rest ==0 and H_rest ==0 and M_rest < 0)):
        result = -1
    else:
        if(M_rest<0):
            H_rest-=1
            M_rest += 60
        if(H_rest<0):
            D_rest-= 1
            H_rest += 24
        result = D_rest*24*60+H_rest*60+M_rest
    print(f'#{t} {result}')