def check(length,word):
    for i in range(length//2+1):
        if word[i] != word[-i-1]:
            return False
    return True


def solution(s):
    for length in range(len(s),0,-1):
        for i in range(len(s)+1-length):
            if check(length,s[i:i+length]):
                return length

solution("abacde")
solution("abcdcba")