def solution(n, lost, reserve):
    arr = [1] * (n+1)
    for r in reserve:
        arr[r] +=1
    for l in lost:
        arr[l] -=1
    
    if arr[1] == 2 and arr[2] == 0:
        arr[1]=arr[2]=1
    if arr[n] == 2 and arr[n-1] ==0:
        arr[n]=arr[n-1]=1
    
    for i in range(2,n):
        if arr[i] == 2:

            if arr[i-1] == 0:
                arr[i-1] = 1
                arr[i] = 1
                continue

            if arr[i+1] == 0:
                arr[i+1] = 1
                arr[i] = 1
                continue
    answer=-1
    for a in arr:
        if a:
            answer+=1
    return answer