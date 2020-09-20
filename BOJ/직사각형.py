import sys
sys.stdin = open("input.txt","r")
for _ in range(4):
    x1,y1,x2,y2,X1,Y1,X2,Y2 = map(int,input().split())
    rec1 = [min(x1,X1),min(y1,Y1),min(x2,X2),min(y2,Y2)]
    rec2 = [max(x1,X1),max(y1,Y1),max(x2,X2),max(y2,Y2)]
    if rec1[2]>=rec2[0] and rec1[3] >= rec2[1]:
        if rec1[2]==rec2[0] and rec1[3] == rec2[1]:
            print('c')
        elif rec1[2]==rec2[0] or rec1[3]==rec2[1]:
            print('b')
        else:
            print('a')
    else:print('d')

