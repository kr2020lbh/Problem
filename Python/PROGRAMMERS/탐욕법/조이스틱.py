# def is_all_A(arr):
#     for a in arr:
#         if a != 'A':
#             return False
#     else: return True
#
# def solution(name):
#
#     cnt = 0
#
#     if ord(name[0]) > 78:
#         cnt += ord('A')-ord(name[0])+26
#     else:
#         cnt += ord(name[0]) - 65
#
#     foward_cnt = backward_cnt = cnt
#
#     for i in range(1,len(name)):
#
#         if  is_all_A(name[i:len(name)]):
#             break
#
#         foward_cnt+=1
#
#         if ord(name[i]) > 78:
#             foward_cnt += ord('A') - ord(name[i]) + 26
#         else:
#             foward_cnt += ord(name[i]) - 65
#
#     for i in range(len(name)-1,0,-1):
#
#         if  is_all_A(name[1:i+1]):
#             break
#
#         backward_cnt+=1
#
#         if ord(name[i]) > 78:
#             backward_cnt += ord('A') - ord(name[i]) + 26
#         else:
#             backward_cnt += ord(name[i]) - 65
#
#     print(foward_cnt,backward_cnt)
#     return min(foward_cnt,backward_cnt)
#
# name = 'JEROEN'
# name1 = 'JAN'
# solution(name)
# solution(name1)
# solution('ABAAB')

def f(start,name):
    counts = []
    for i in range(len(name)):
        cnt = 0
        if name[i] != 'A':
            right = abs(i-start)
            left = len(name)-right
            cnt += min(right,left)
            counts.append([cnt,i])
    if len(counts)==0:
        return None
    return sorted(counts,key=lambda x:x[0])[0]


def solution(name):
    name= list(name)
    res = 0

    start = 0

    while f(start,name) != None:
        cnt,start = f(start,name)
        res+=cnt
        if ord(name[start]) > 78:
            res += ord('A') - ord(name[start]) + 26
        else:
            res += ord(name[start]) - 65
        name[start] = 'A'
    return res

name = 'JEROEN'
name1 = 'AAABAB'
solution(name)
solution(name1)
solution('ABBAAAAAB')
