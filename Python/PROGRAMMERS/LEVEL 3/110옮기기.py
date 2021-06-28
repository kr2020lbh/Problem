def findword(word):
    result = []
    for i in range(0,len(word)-2):
        if word[i:i+3] == '110':
            result.append(i)
    return result


def solution(s):
    answer = []
    for word in s:
        for i in findword(word):
            print(i)
    return answer


solution(["1110","100111100","0111111010"]	)