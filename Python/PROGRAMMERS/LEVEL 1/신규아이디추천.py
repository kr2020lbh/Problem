import re


def solution(new_id):
    answer = re.sub('[^a-z\d\-\_\.]','',new_id.lower())
    answer = re.sub('\.{2,}','.',answer)
    answer = re.sub('^\.|\.$','',answer)
    if answer == '':
        answer = 'a'
    if len(answer) > 15:
        answer = re.sub('\.$','',answer[0:15])
    while len(answer) < 3:
        answer += answer[-1]
    return answer




solution('...!@BaT#*..y.abcdefghijklm')
solution('z-+.^.')