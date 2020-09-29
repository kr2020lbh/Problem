import sys
sys.stdin = open("input.txt","r")

def get_possible_bracket(depth,cur_depth,cur):
    if cur_depth == depth:
        indexes.append(cur)
    else:
        for i in range(2):
            if cur[-1] == 1:
                if i==1:
                    continue
            get_possible_bracket(depth,cur_depth+1,cur+[i])


def f(arr,index):
    i = 0
    while i < len(index)-1:
        k = (i + 1) * 2 - 1
        if index[i] == 0 and index[i+1]==0:
            flag = True
            if i !=0:
                res = cacluator(res,arr[k+1],arr[k])
            else:
                res = cacluator(arr[k-1],arr[k+1],arr[k])
            i += 1

        else: #index[i]==0 and index[i]==1

            flag = False
            if i !=0:
                res = cacluator(res,cacluator(arr[k+1],arr[k+3],arr[k+2]),arr[k])
            else:
                res = cacluator(arr[k-1],cacluator(arr[k+1],arr[k+3],arr[k+2]),arr[k])
            i += 2
    if flag:
        res = cacluator(res, arr[-1], arr[-2])
    else:
        if i == len(index)-1:
            res = cacluator(res, arr[-1], arr[-2])
    return res


def cacluator(l_v,r_v,operator):
    l_v = int(l_v)
    r_v = int(r_v)
    if operator == '+': return l_v+r_v
    if operator == '*': return l_v*r_v
    if operator == '-': return l_v-r_v


N = int(input())
arr = list(input())
indexes = []
if N > 3:
    depth = (N - 1) // 2  # 연산자 수
    for i in range(2):
        get_possible_bracket(depth,1,[i])

    MAX = -2**31
    for index in indexes:
        res = f(arr,index)
        if MAX < res:
            MAX = res
    print(MAX)
else:
    if N == 1:
        print(*arr)
    else:
        print(cacluator(arr[0],arr[2],arr[1]))
