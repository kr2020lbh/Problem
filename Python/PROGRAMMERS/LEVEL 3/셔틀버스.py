def solution(n, t, m, timetable):
    timetable = sorted(list(map(lambda x:(int(x[0:2]) *60+ int(x[3:5])), timetable )))
    first_bus = 9*60
    idx = 0

    for i in range(n):
        cur_bus_time = first_bus + i*t
        bus = []
        while idx < len(timetable):
            crew_time = timetable[idx]
            if cur_bus_time < crew_time:
                break
            else:
                if len(bus) < m:
                    bus.append(crew_time)
                    idx += 1
                else:
                    break

    if len(bus) == m:
        answer = bus[-1]-1
    else:
        answer = cur_bus_time

    h,m = str(answer//60), str(answer%60)
    new_h = '0' + h if len(h) == 1 else h
    new_m = '0' + m if len(m) == 1 else m
    return new_h+':'+new_m

n1,t1,m1,timetable1 = [1,1,5,["08:00", "08:01", "08:02", "08:03"]]
n2,t2,m2,timetable2 = [10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]]
solution(n1,t1,m1,timetable1)
solution(n2,t2,m2,timetable2)