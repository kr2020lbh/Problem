def solution(msg):
    alphabet = dict()
    answer = []

    for i in range(26):
        alphabet[chr(65+i)]=i+1
    i = 0
    while i < len(msg):
        j = i
        while j <= len(msg):
            j += 1
            if msg[i:j] not in alphabet:
                j -= 1
                break
        answer.append(alphabet[msg[i:j]])
        if j >= len(msg):
            break
        w = msg[i:j]
        c = msg[j]
        alphabet[w+c] = len(alphabet) + 1
        i = j
    return answer

msg = 'TOBEORNOTTOBEORTOBEORNOT'
solution(msg)