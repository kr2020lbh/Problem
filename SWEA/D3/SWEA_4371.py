import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    total = []
    cnt = 0
    numbers =[ int(input()) for i in range(int(input()))]
    total = [numbers]    
    total.append([False]*len(numbers))
    total[1][0] = True

    for idx,day in enumerate(total[0]):
        
        if total[1][idx]==True:
            continue
        jump = day -1

        cnt+=1
        
        while(day in total[0]):
            total[1][total[0].index(day)]=True
            day+=jump

    print(f'#{t} {cnt}')