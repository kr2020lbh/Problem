def solution(progresses, speeds):
    days = []
    for i in range(len(speeds)):
        day = (100 - progresses[i]) % speeds[i]
        if day == 0:
            days.append((100 - progresses[i]) // speeds[i])
        else:
            days.append((100 - progresses[i]) // speeds[i] + 1)
    answer = []
    i = 0
    while i < len(days):
        cnt = 0
        for j in range(i, len(days)):
            if days[i] >= days[j]:
                cnt += 1
            else:
                j -= 1
                break
        answer.append(cnt)
        i = j + 1
    return answer


def solution(progresses, speeds):
    days = []
    Q=[]
    for i in range(len(speeds)):
        day = (100-progresses[i])%speeds[i]
        if day == 0:
            days.append((100-progresses[i])//speeds[i])
        else:
            days.append((100-progresses[i])//speeds[i]+1)
        if (not Q) or (Q[-1][0]<days[-1]) :
            Q.append([days[-1],1])
        else:
            Q[-1][1]+=1

    return [q[1] for q in Q]

#100에서 값을 뺴고, 각각 speeds로 나눈다.
#이때 나눠떨어지면 바로, 아니면 +1

progresses = [93, 30, 55]
# progresses =[95, 90, 99, 99, 80, 99]
speeds = [1,30,5]
# speeds = [1, 1, 1, 1, 1, 1]
solution(progresses,speeds)