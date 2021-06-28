def StringtoInt(time):
    H,M,S = time.split(':')
    times = int(H)*3600 +int(M) * 60 + int(S)
    return times

def InttoString(time):
    H = time // 3600
    M = (time - H*3600) // 60
    S = (time - H*3600 - M * 60)
    return '{}:{}:{}'.format(convert(H),convert(M),convert(S))

def convert(num):
    if num < 10:
        return str('0' + str(num))
    else:
        return str(num)

def solution(play_time, adv_time, logs):
    timeArr = [0] * (StringtoInt(play_time)+1)
    for log in logs:
        start,end = log.split('-')
        timeArr[StringtoInt(start)] += 1
        timeArr[StringtoInt(end)] -= 1

    for i in range(1,len(timeArr)):
        timeArr[i] = timeArr[i] + timeArr[i-1]

    for i in range(1,len(timeArr)):
        timeArr[i] = timeArr[i] + timeArr[i-1]

    advTime = StringtoInt(adv_time)

    maxSum = 0
    maxIdx = 0

    for i in range(advTime-1,len(timeArr)):
        if i >= advTime:
            if maxSum < timeArr[i] - timeArr[i - advTime]:
                maxSum = timeArr[i] - timeArr[i - advTime]
                maxIdx = i - advTime + 1
        else:
            if maxSum < timeArr[i]:
                maxSum = timeArr[i]
                maxIdx = i - advTime + 1

    return InttoString(maxIdx)
pt1 = "02:03:55"
at1 = "00:14:15"
logs1 = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

solution(pt1,at1,logs1)
solution("99:59:59","25:00:00",	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])