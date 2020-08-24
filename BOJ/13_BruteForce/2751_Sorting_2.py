import sys
sys.stdin = open("input.txt","r")
def merge_sort(arr,start,end):
    middle = (start + end) // 2
    if start<middle:
        print(start, end)

        merge_sort(arr,start,middle)
        merge_sort(arr,middle,end)
        merge(arr,start,middle,end)
    else:
        return
def merge(arr,start,middle,end):
    tmp_left = arr[start:middle+1]
    tmp_right = arr[middle+1:end]
    print(start, middle, end, tmp_left, tmp_right)
    i=j=0
    k=start
    while i<middle+1-start and j<end-middle:

        if tmp_left[i]<=tmp_right[j]:
            arr[k] = tmp_left[i]
            i+=1
        else:
            arr[k] = tmp_right[j]
            j+=1
        k+=1
    while i<middle+1:
        arr[k] = tmp_left[i]
        i+=1
        k+=1
    while j<end:
        arr[k] = tmp_right[j]
        j+=1
        k+=1


li = []
for i in range(int(input())):
    li.append(int(input()))
print(li)
merge_sort(li,0,len(li))
