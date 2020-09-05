import sys
sys.stdin=open("input.txt","r")

l = '('
r = ')'
def check_balance(arr):
    l_cnt=r_cnt=0
    for element in arr:
        if element == l:
            l_cnt+=1
        if element == r:
            r_cnt+=1
    if l_cnt==r_cnt:
        return True
    return False
def check_alright(arr):
    S=[]
    for element in arr:
        if element == l:
            S.append(l)
        if element == r:
            if not S:
                return False
            if l!=S.pop():
                return False
    if S:
        return False
    return True

'''
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.
'''
# def recur(w):
#     for i in range(1, len(w) + 1):
#         if check_balance(w[0:i]) and check_balance(w[i::]):
#             u = w[0:i]
#             v = w[i::]
#             if check_alright(u):
#                 u+=recur(v)
#                 return u
#             else:
#                 return '('+recur(v)+')'+refine_u(u)
#     else:
#         return ''
# def refine_u(w):
#     w = list(w)
#     ans = w[1:len(w)-1:1]
#     for i in range(len(ans)):
#         if ans[i] ==l:
#             ans[i]=r
#         else:
#             ans[i]=l
#     return ''.join(ans)
#
# for t in range(int(input())):
#     w = input()
#     print(w,recur(w))
#


l = '('
r = ')'

def check_balance(arr):
    l_cnt=r_cnt=0
    for element in arr:
        if element == l:
            l_cnt+=1
        if element == r:
            r_cnt+=1
    if l_cnt==r_cnt:
        return True
    return False

def check_alright(arr):
    S=[]
    for element in arr:
        if element == l:
            S.append(l)
        if element == r:
            if not S:
                return False
            if l!=S.pop():
                return False
    if S:
        return False
    return True


def recur(w):
    for i in range(1, len(w) + 1):
        if check_balance(w[0:i]) and check_balance(w[i::]):
            u = w[0:i]
            v = w[i::]
            if check_alright(u):
                u += recur(v)
                return u
            else:
                return '(' + recur(v) + ')' + refine_u(u)
    else:
        return ''

def refine_u(w):
    w = list(w)
    ans = w[1:len(w) - 1:1]
    for i in range(len(ans)):
        if ans[i] == l:
            ans[i] = r
        else:
            ans[i] = l
    return ''.join(ans)


def solution(p):
    answer = recur(p)
    return answer