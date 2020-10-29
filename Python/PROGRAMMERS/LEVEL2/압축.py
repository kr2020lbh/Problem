def solution(msg):
    alphabet = dict()
    for i in range(26):
        alphabet[chr(65+i)]=i+1
    i=0
    cur = msg[i]
    while i < len(msg)-1:
        print(alphabet[cur])

        if alphabet.get(cur + msg[i+1]):
            cur += msg[i+1]

        else:
            alphabet[cur+msg[i+1]] = len(alphabet)+1
            cur = msg[i+1]
        i+=1




    answer = []
    return answer

msg = 'KAKAO'
solution(msg)