# from itertools import combinations
# def check_contain(used_key,cur_key):
#     if len(used_key) < len(cur_key):
#         for u in used_key:
#             for c in cur_key:
#                 if u == c:
#                     break
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# def check_key(used_key,cur_key,bool_arr):
#     for u in used_key:
#         if check_contain(u,cur_key):
#             return False
#     for i in range(len(bool_arr[0])):
#         tmp = False
#         for k in cur_key:
#             tmp = tmp or bool_arr[k][i]
#         if tmp == False:
#             return False
#     return True
#
#
# def solution(relation):
#     answer = 0
#     new_relation = [list(r) for r in zip(*relation)]
#     bool_arr = [[True]*len(new_relation[0]) for _ in range(len(new_relation))]
#     # [print(a) for a in new_relation]
#     for row in range(len(new_relation)):
#         for col in range(len(new_relation[0])):
#             if new_relation[row][col] in new_relation[row][col+1::]:
#                 bool_arr[row][col] = False
#
#     indexes = set()
#
#     for i in range(len(bool_arr)):
#         if sum(bool_arr[i]) == len(bool_arr[i]):
#             indexes.add(i)
#     answer += len(indexes)
#     indexes = list(set(range(len(relation[0])))-indexes)
#
#
#     keys = []
#     used = []
#     for i in range(2,len(relation)+1):
#         keys += map(list,combinations(indexes,i))
#
#     for key in keys:
#         if check_key(used,key,bool_arr):
#             used.append(key)
#             answer += 1
#     return answer
from itertools import combinations

def check_contain(used_key,key):
    if not used_key:
        return False

    for uk in used_key:
        cnt = 0
        for u in uk:
            if u in key:
                cnt += 1

        if cnt == len(uk):
            return True
    return False

#check contain이 True이면 그 key는 하지마
def check_key(used_key,key,relation):
    if check_contain(used_key,key):
        return False
    new_col = set()
    for i in range(len(relation)):
        tmp = ''
        for k in key:
            tmp+=relation[i][k]
        new_col.add(tmp)
    if len(new_col) == len(relation):
        return True
    return False





def solution(relation):
    answer = 0


    del_idx = []
    for i in range(len(relation[0])):
        tmp = set()
        for j in range(len(relation)):
            tmp.add(relation[j][i])
        if len(tmp) == len(relation):
            del_idx.append(i)

    answer += len(del_idx)
    for i in del_idx[::-1]:
        for j in range(len(relation)):
            del relation[j][i]


    comb = []
    used_key = []
    if relation:
        for i in range(2,len(relation[0])+1):
            comb += map(list,combinations(range(len(relation[0])),i))

        for key in comb:
            if check_key(used_key,key,relation):
                answer += 1
                used_key += [key]
    return answer


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(relation)