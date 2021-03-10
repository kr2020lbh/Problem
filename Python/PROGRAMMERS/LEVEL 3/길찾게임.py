def solution(nodeinfo):

    for i in range(len(nodeinfo)):
        nodeinfo[i] += [i+1]
    nodeinfo.sort(key=lambda x:(-x[1],x[0]))
    stack1 = []
    idx = 0


    while idx < len(nodeinfo):
        tmp_idx = idx
        if tmp_idx == 0:
            stack1.append(0)
        else:
            flag = False
            while tmp_idx < len(nodeinfo):
                cur_node = nodeinfo[tmp_idx]

                tmp_idx += 1

        idx += 1
        prev_node = nodeinfo[idx]



solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	)
