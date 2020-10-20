#10761. 신뢰
import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    input_list = list(input().split())
    B = []
    B_SUM = 0
    O = []
    O_SUM = 0
    for i in range(1,int(input_list[0])+1):
        if input_list[2*i-1] == 'B':
            B.append(int(input_list[2*i]))
        else:
            O.append(int(input_list[2*i]))

    if len(B):
        B_SUM = len(B) + B[0] - 1
        for i in range(1,len(B)):
            B_SUM += abs(B[i] - B[i-1])

    if len(O):
        O_SUM = len(O) + O[0] - 1
        for i in range(1,len(O)):
            O_SUM += abs(O[i] - O[i-1])

    print("#{} {}".format(t,max(B_SUM,O_SUM)))