def get_set(str1):
    sets = [[0]*26 for _ in range(26)]
    for i in range(1,len(str1)):
        if is_small(str1[i-1]):
            if is_small(str1[i]):
                # element = str1[i-1] + str1[i]
                sets[ord(str1[i-1])-97][ord(str1[i])-97] += 1
                continue
            if is_big(str1[i]):
                # element = str1[i-1] + chr(ord(str1[i])+32)
                sets[ord(str1[i-1])-97][ord(str1[i])+32-97] += 1
                continue
        if is_big(str1[i-1]):
            if is_small(str1[i]):
                # element = chr(ord(str1[i-1])+32) + str1[i]
                sets[ord(str1[i-1])+32-97][ord(str1[i])-97] += 1
                continue
            if is_big(str1[i]):
                # element = chr(ord(str1[i-1])+32) + chr(ord(str1[i])+32)
                sets[ord(str1[i-1])+32-97][ord(str1[i])+32-97] += 1
                continue
    return sets


def is_small(char):
    if 97 <= ord(char) <= 122:
        return True
    return False


def is_big(char):
    if 65 <= ord(char) <= 90:
        return True
    return False

def solution(str1, str2):
    a = get_set(str1)
    b = get_set(str2)
    union = 0
    intersection = 0
    for i in range(26):
        for j in range(26):
            if a[i][j]:
                if b[i][j]:
                    union += max(a[i][j],b[i][j])
                    intersection += min(a[i][j],b[i][j])
                else:
                    union += a[i][j]
            if b[i][j]:
                    union += b[i][j]


    if union == 0:
        return 65536
    return int((intersection/union)*65536)

print(solution('aa1+aa2','AAAA12'))

