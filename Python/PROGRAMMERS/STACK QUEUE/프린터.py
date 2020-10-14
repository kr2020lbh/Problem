def solve(p,l):
    cnt=1
    while True:
        element = p.pop(0)
        for i in range(len(p)):
            if element[0] < p[i][0]:
                p.append(element)
                break
        else:
            if element[1] == l:
                return cnt
            cnt+=1


def solution(priorities, location):
    new_p = []
    for i in range(len(priorities)):
        new_p.append([priorities[i],i])
    return solve(new_p,location)


p1 = [1, 1, 9, 1, 1, 1]
l1 = 0
p2 = [2,1,3,2]
l2 = 2

print(solution(p2,l2))