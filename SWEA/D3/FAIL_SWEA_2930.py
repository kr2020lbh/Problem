#힙
import sys
sys.stdin = open("input.txt","r")
class Myheap:
    length = 1

    def insert_heap(self,arr,n):
        i=1
        while True:
            if arr[i]==0:
                arr[i] = n
                self.length += 1
                break
            else:
                i+=1
        while i!=1:
            if arr[i]>arr[(i-1)//2]:
                arr[i],arr[(i-1)//2]=arr[(i-1)//2],arr[i]
                i = (i-1)//2
                continue
            break

    def pop_heap(self,arr):
        tmp = arr[1]
        arr[1]=arr[self.length+1]
        arr[self.length+1]=0
        self.length -= 1
        while arr[i]<arr[2*i] or arr[i]<arr[2*i+1]:
            if arr[2*i]>=arr[2*i+1]:
                arr[i],arr[2*i] = arr[2*i],arr[i]
            else:
                arr[i],arr[2*i+1] = arr[2*i+1],arr[i]
            i+=1


for t in range(1,int(input())+1):
    N = int(input())
    arr = [0] * (N+1)
    heap = Myheap()
    action = list(map(int,input().split()))
    if action[0]:
        heap.insert_heap(arr,action[1])
    else:
        pass
