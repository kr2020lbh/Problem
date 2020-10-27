from itertools import combinations

def check(candidate_key,comb):
    for i in range(1, len(comb) + 1):
        for c_key in candidate_key:
            if c_key in list(map(list, combinations(comb, i))):
                return False
    return True


def is_candidate(relation,comb):
    res = []
    for i in range(len(relation)):
        tmp = ''
        for j in comb:
            tmp += relation[i][j]
        res.append(tmp)
    if len(set(res)) == len(res):
        return True
    else: return False


def solution(relation):
    candidate_key = []
    used_key = [0]*len(relation[0])
    col_to_row_list = list(zip(*relation))
    for i in range(len(col_to_row_list)):
        if len(set(col_to_row_list[i])) == len(col_to_row_list[i]):
            used_key[i] = 1
            candidate_key.append([i])

    for colum_nums in range(2,len(used_key)+1):
        for comb in combinations(range(len(used_key)), colum_nums):
            if check(candidate_key,comb):
                print('yes')
                if is_candidate(relation,comb):
                    candidate_key.append(list(comb))
            else:
                print('no')

            print(candidate_key,comb)

    return len(candidate_key)
#
#
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(relation)
