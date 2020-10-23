from collections import Counter

def cut(cut_len,s):
    tmp = []
    for i in range(0,len(s),cut_len):
        tmp.append(''.join(s[i:i+cut_len]))
    c = Counter(tmp)
    res = ''
    for key,value in c.items():
        if value == 1:
            res += key
        else:
            res += str(value) + key
    print(res)
    return len(res)


def solution(s):
    s = list(s)
    for i in range(len(s)//2,1,-1):
        length = cut(i,s)
        if length:
            return length
    else: return len(s)

solution('aabbaccc')