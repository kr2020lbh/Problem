def solution(lines):
    logs = []
    for line in lines:
        date,time,duration = line.split()
        hour,min,sec = time.split(":")
        end_time = (int(hour)*60*60 + int(min)*60 + float(sec)) * 1000
        logs.append([end_time - float(duration[:-1]) * 1000+1, end_time])
    cnt_max = 1
    for i in range(len(logs)-1):
        cnt = 1
        for j in range(i+1,len(logs)):
            if logs[j][0]- logs[i][1] < 1000:
                cnt += 1
        cnt_max = max(cnt_max,cnt)
    return cnt_max


lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s",
         "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s",
         "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
         "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s",
         "2016-09-15 21:00:00.966 0.381s","2016-09-15 21:00:02.066 2.62s"]

# solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
solution(lines)