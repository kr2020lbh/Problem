def solution(s):
    answer = [0,0]
    while s != '1':
        length,zeroes = len(s),s.count('0')
        s = bin(length-zeroes)[2:]
        answer[0],answer[1] = answer[0]+1,answer[1]+zeroes
    return answer



solution('110010101001')
solution('01110')
solution('1111111')