# #힙
import sys
sys.stdin = open("input.txt","r")

class Myheap:
    length = 0
    def __init__(self,n):
        self.arr = [0] * (n+1)
    def insert_heap(self,element):
        self.length += 1
        idx = self.length
        self.arr[idx] = element
        while True:
            if idx == 1:
                break
            else:
                parent_idx = idx//2
                if self.arr[idx]>self.arr[parent_idx]:
                    self.arr[idx],self.arr[parent_idx]=self.arr[parent_idx],self.arr[idx]
                    idx = parent_idx
                else:
                    break
    def delete_heap(self):
        if self.length == 0:
            return -1
        pop_value = self.arr[1]
        self.arr[1] = self.arr[self.length]
        self.arr[self.length] = 0
        self.length -= 1
        idx = 1
        while idx<self.length:
            if self.arr[idx] < self.arr[idx*2] or self.arr[idx] < self.arr[idx*2+1]:
                if self.arr[idx*2] > self.arr[idx*2+1]:
                    self.arr[idx],self.arr[idx*2]  = self.arr[idx*2] ,self.arr[idx]
                    idx = idx*2
                else:
                    self.arr[idx], self.arr[idx * 2 +1 ] = self.arr[idx * 2 + 1], self.arr[idx]
                    idx= idx*2 + 1
            else:
                break
        return pop_value

for t in range(1,int(input())+1):
    N = int(input())
    arr = ''
    heap = Myheap(N)
    for _ in range(N):
        action = list(map(int,input().split()))
        if action[0]==1:
            heap.insert_heap(action[1])
        else:
            arr+=str(heap.delete_heap())+' '
    print(f'#{t} {arr}')