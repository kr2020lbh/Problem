def func(commands,db):

    if len(commands) == 3:
        command,id,nickname = commands
        if command == 'Enter':
            db[id] = nickname
            string = [id,'님이 들어왔습니다.']
        if command == 'Change':
            db[id] = nickname
            string = None
    else:
        command,id = commands
        string = [id,'님이 나갔습니다.']
    return db,[string]


def solution(record):
    answer = []
    db = dict()

    for r in record:
        commands = r.split()
        if commands[0] == 'Enter':
            db[commands[1]] = commands[2]
            answer.append([commands[1],'님이 들어왔습니다.'])
            continue

        if commands[0] == 'Change':
            db[commands[1]] = commands[2]
            continue

        if commands[0] == 'Leave':
            answer.append([commands[1], '님이 나갔습니다.'])
            continue

    for i in range(len(answer)):
        answer[i] = db[answer[i][0]] + answer[i][1]
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])