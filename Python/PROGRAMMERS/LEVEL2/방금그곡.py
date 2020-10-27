def concat_sharp(string):
    res = []
    for i in range(1, len(string)):
        if string[i] == '#':
            res.append(string[i - 1] + string[i])
        else:
            if string[i - 1] != '#':
                res.append(string[i - 1])
    if string[-1] != "#":
        res.append(string[-1])
    return res


def check(m,music):
    cnt = 0
    for i in range(len(music)):
        if cnt == len(m):
            return True
        if m[cnt] == music[i]:
            cnt += 1
        else:
            cnt = 0
            if m[cnt] == music[i]:
                cnt += 1
    if cnt == len(m):
        return True
    return False


def solution(m, musicinfos):
    answer = [[] for _ in range(2000)]
    for music in musicinfos:
        time1, time2, title, melody = music.split(',')
        new_melody = concat_sharp(melody)
        new_m = concat_sharp(m)

        h1, m1 = int(time1[0:2]), int(time1[3:5])
        h2, m2 = int(time2[0:2]), int(time2[3:5])
        minute = (h2 - h1) * 60
        tmp_minute = m2 - m1


        total_minute = minute + tmp_minute
        q = total_minute // len(new_melody)
        r = total_minute % len(new_melody)
        total_melody = q * new_melody + new_melody[0:r]
        if check(new_m,total_melody):
            answer[total_minute].append(title)

    for title in answer[::-1]:
        if title:
            return title[0]
    return '(None)'