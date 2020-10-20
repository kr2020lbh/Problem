def solution(arr1, arr2):
    row1 = len(arr1)
    col1 = len(arr1[0])
    row2 = len(arr2)
    col2 = len(arr2[0])
    answer = []
    for i in range(row1):
        tmp = []

        for j in range(col2):
            SUM = 0
            for k in range(col1):
                SUM += arr1[i][k]*arr2[k][j]
            tmp.append(SUM)
        answer.append(tmp)
    return answer
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
solution([[1,2,3,4],[1,2,3,4]],[[1,2],[3,4],[5,6],[7,8]])
print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))