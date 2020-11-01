def solution(n, delivery):
    is_left = ['O'] + ['?'] *(n)
    delivery.sort(key=lambda x:(-x[-1],x[0]))
    for i in range(len(delivery)):
        a,b,check = delivery[i]
        if check == 1:
            is_left[a] = 'O'
            is_left[b] = 'O'
            continue
        if check == 0:
            if is_left[a] == 'O':
                is_left[b] = 'X'
            elif is_left[b] == 'O':
                is_left[a] = 'X'
    return ''.join(is_left[1::])

delivery = [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]
solution(7,delivery)
solution(6,[[1,3,1],[3,5,0],[5,4,0],[2,5,0]])