comp1 = input()
comp2 = input()
res = [[0] * (len(comp2) + 1) for _ in range(len(comp1) + 1)]

for i in range(len(comp1)):
    for j in range(len(comp2)):
        if comp1[i] == comp2[j]:
            res[i+1][j+1] = res[i][j] + 1
        else:
            res[i+1][j+1] = max(res[i][j+1],res[i+1][j])
ans=''
i=len(comp1)
j=len(comp2)
while i != 0 and j != 0:
    if comp1[i-1] == comp2[j-1]:
        ans = comp1[i-1] + ans
        i -= 1
        j -= 1
        continue
    if res[i][j-1] < res[i-1][j]:
        i -= 1
    else:
        j -= 1
print(res[-1][-1])
print(ans)