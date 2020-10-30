def get_idx(a):
    res = []
    for i in range(len(a)):
        res.append([a[i],i])
    return sorted(res)
def solution(a):
    if len (a) <= 3:
        return len(a)
    else:
        minv = a[0]
        idx = []
        for i in range(1,len(a)-1):
            if a[i] < minv:
                minv = a[i+1]+1
                idx.append(i)
        print(idx)
    return len(idx)+2
solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]	)