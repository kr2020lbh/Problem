def solution(operations):
    arr = []
    for op in operations:
        s,n = op.split()
        if s == 'I':
            arr.append(int(n))
        else:
            if arr:
                if int(n) == -1:
                    arr.pop(0)
                else:
                    arr.pop(-1)
        arr.sort()
    return [max(arr),min(arr)] if arr else [0,0]


solution(	["D -45", "D 653", "D 1", "D -642", "D 45", "I 97", "D 1", "D -1", "D 333"])