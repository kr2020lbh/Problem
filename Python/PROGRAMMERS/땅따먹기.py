def solution(land):
    for row in range(1,len(land)):
        for i in range(4):
            areas = [area for area in land[row-1]]
            areas.remove(land[row-1][i])
            land[row][i] += max(areas)

    return max(land[len(land)-1])
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1],[5,6,7,8],[4,3,2,1]]))