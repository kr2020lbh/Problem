def solution(triangle):
    for i in range(len(triangle) - 1):
        tmp = []
        for j in range(len(triangle[i + 1])):
            if j == 0:
                tmp.append(triangle[i][j] + triangle[i + 1][j])
                continue

            if j == len(triangle[i + 1]) - 1:
                tmp.append(triangle[i][j - 1] + triangle[i + 1][j])
                continue

            tmp.append(max(triangle[i][j] + triangle[i + 1][j], triangle[i][j - 1] + triangle[i + 1][j]))
        triangle[i + 1] = tmp[::]
    return max(tmp)

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

for i in range(len(triangle)-1):
    tmp  = []
    for j in range(len(triangle[i+1])):
        if j == 0:
            tmp.append(triangle[i][j] + triangle[i+1][j])
            continue

        if j == len(triangle[i+1])-1:
            tmp.append(triangle[i][j-1] + triangle[i + 1][j])
            continue

        tmp.append(max(triangle[i][j] + triangle[i+1][j],triangle[i][j-1] + triangle[i + 1][j]))
    triangle[i + 1] = tmp[::]
print(tmp)
