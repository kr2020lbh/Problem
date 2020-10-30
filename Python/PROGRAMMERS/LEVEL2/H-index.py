from collections import Counter
def solution(H):
    H = dict(Counter(H))
    H = sorted(H.items())

    cnts = [0]*len(H)
    cnts[0] = H[0][1]
    for i in range(1,len(H)):
        cnts[i] = cnts[i-1] + H[i][1]

    for i in range(len(H)-1,0,-1):
        lte = cnts[i-1]
        gte = cnts[-1] - lte

        for h_index in range(H[i][0],H[i-1][0],-1):
            if lte <= h_index and gte >=h_index:
                return h_index
    lte = 0
    gte = cnts[-1]

    for h_index in range(H[0][0], -1, -1):
        if lte <= h_index and gte >= h_index:
            return h_index

print(solution([3, 0, 6, 1, 5]))
print(solution([0, 1, 9]))
print(solution([5,5,5,5]))
print(solution([10,11,12,13]))
print(solution([66,31]))