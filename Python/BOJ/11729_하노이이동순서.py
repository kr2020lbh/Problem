def hanoi(n,start,temp,end):
    global cnt
    cnt += 1
    if n == 1:
        p.append([start,end])
        return
    hanoi(n-1,start,end,temp)
    p.append([start,end])
    hanoi(n-1,temp,start,end)

cnt = 0
p = []
hanoi(int(input()),1,2,3)
print(cnt)
for element in p:
    print(*element)