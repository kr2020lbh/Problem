from copy import deepcopy
def solution(info, query):
    new_info = []
    answer = []
    for i in info:
        new_info.append(i.split(' '))
    for q in query:
        tmp = q.split(' ')
        score = int(tmp[-1])
        lang, position, career, food = tmp[0], tmp[2], tmp[4], tmp[6]
        selected = []

        if lang != '-':
            for i in new_info:
                if i[0] == lang:
                    selected.append(i)
        else:
            selected = deepcopy(new_info)
        if position != '-':
            i = 0
            while i < len(selected):
                if selected[i][1] != position:
                    selected.pop(i)
                else:
                    i += 1
        if career != '-':
            i = 0
            while i < len(selected):
                if selected[i][2] != career:
                    selected.pop(i)
                else:
                    i += 1

        if food != '-':
            i = 0
            while i < len(selected):
                if selected[i][3] != food:
                    selected.pop(i)
                else:
                    i += 1
        cnt = 0

        for s in selected:
            if int(s[-1]) >= score:
                cnt += 1
        answer.append(cnt)
    return answer

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
solution(info,query)

