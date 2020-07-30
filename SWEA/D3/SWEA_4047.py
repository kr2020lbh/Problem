import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    result = {'S':13,'D':13,'H':13,'C':13} # S D H C
    mydecks = input()
    mydeck = []
    flag = True
    for i in range(len(mydecks)//3):
        mydeck.append((mydecks[i*3:(i+1)*3]))
        result[mydecks[i*3]]-=1

    for card in mydeck:
        if mydeck.count(card)>1:
            flag = False
            break

    result = list(result.values())
    
    if flag == True:
        print(f'#{t} {result[0]} {result[1]} {result[2]} {result[3]}')
    else:
        print(f'#{t} ERROR')
        