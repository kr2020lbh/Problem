import sys
sys.stdin = open("input.txt","r")

def get_index(r,c):
    return max(abs(r),abs(c))

def get_pivot_num(region):
    return (region*2 + 1) ** 2

def get_num(r,c,index,pivot_num):
    if r == index:
        return pivot_num - (index - c)
    if c == -index:
        return pivot_num - (2*index + ( index - r ))
    if r == -index:
        return pivot_num - (4*index + ( index + c ))
    if c == index:
        return pivot_num - (6*index + ( index + r ))

r1,c1,r2,c2 = map(int,input().split())
MAX = 0
ans = []
for i in range(r1,r2+1):
    row = []
    for j in range(c1,c2+1):
        index = get_index(i,j)
        pivot_num = get_pivot_num(index)
        num = get_num(i,j,index,pivot_num)
        row.append(num)
        if num > MAX:
            MAX = num
    ans.append(row)
max_str = len(str(MAX))

for i in range(len(ans)):
    tmp = []
    for j in range(len(ans[0])):
        tmp_str_num = str(ans[i][j])
        if len(tmp_str_num) < max_str:
            tmp_str_num = ' '*(max_str-len(tmp_str_num)) + tmp_str_num
        tmp.append(tmp_str_num)
    print(*tmp)