zero = 0
one = 0

def check(arr,row,col,length):
    global zero,one

    if length == 1:
        if arr[row][col] == 1:
            one += 1
        else:
            zero += 1
        return

    else:
        first = arr[row][col]
        flag = True
        for i in range(row,row+length):
            for j in range(col,col+length):
                if arr[i][j] != first:
                    flag = False
                    break
            if flag == False:
                break
        if flag:

            if first == 1:
                one += 1
            else:
                zero += 1
        else:
            for r,c in [[row,col],[row,col+length//2],[row+length//2,col],[row+length//2,col+length//2]]:
                check(arr,r,c,length//2)


def solution(arr):
    global zero,one
    check(arr,0,0,len(arr))
    answer = [zero, one]
    return answer

arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
solution(arr)