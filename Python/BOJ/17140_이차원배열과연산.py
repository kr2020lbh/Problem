import sys
sys.stdin = open("input.txt","r")
def R():
    new_arr = []
    max_length = 0
    row = len(arr)
    col = len(arr[0])
    for i in range(row):
        tmp_dict = dict()
        for j in range(col):
            if arr[i][j] == 0 : continue
            if tmp_dict.get(arr[i][j]):
                tmp_dict[arr[i][j]] += 1
            else:
                tmp_dict[arr[i][j]] = 1
        if max_length < len(tmp_dict)*2:
            max_length = len(tmp_dict)*2
        tmp_arr = []
        if len(tmp_dict) > 100:
            tmp_dict = tmp_dict[0:100]
        for num,cnt in sorted(tmp_dict.items(),key=lambda x:(x[1],x[0])):
            tmp_arr.extend([num,cnt])
        new_arr.append(tmp_arr)
    row = len(new_arr)
    for i in range(row):
        new_arr[i] = new_arr[i] + [0]*(max_length-len(new_arr[i]))

    return new_arr

def C():
    new_arr = []
    max_length = 0
    row = len(arr)
    col = len(arr[0])
    for j in range(col):
        tmp_dict = dict()
        for i in range(row):
            if arr[i][j] == 0 : continue
            if tmp_dict.get(arr[i][j]):
                tmp_dict[arr[i][j]] += 1
            else:
                tmp_dict[arr[i][j]] = 1
        if max_length < len(tmp_dict)*2:
            max_length = len(tmp_dict)*2
        tmp_arr = []
        if len(tmp_dict) > 100:
            tmp_dict = tmp_dict[0:100]
        for num,cnt in sorted(tmp_dict.items(),key=lambda x:(x[1],x[0])):
            tmp_arr.extend([num,cnt])
        new_arr.append(tmp_arr)
    row = len(new_arr)
    for i in range(row):
        new_arr[i] = new_arr[i] + [0]*(max_length-len(new_arr[i]))

    return list(map(list,zip(*new_arr)))
r,c,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(3)]
answer = 0
r -= 1
c -= 1
while answer <= 100:
    if 0<= r < len(arr) and 0<= c < len(arr[0]) and arr[r][c] == k:
        break
    else:
        if len(arr) >= len(arr[0]):
            arr = R()
        else:
            arr = C()
    answer += 1
if answer > 100:
    print(-1)
else:
    print(answer)
