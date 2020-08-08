# #힙
import sys
sys.stdin = open("input.txt","r")

# class Myheap:
#     length = 0
#     def __init__(self,n):
#         self.arr = [0] * (n+1)
#     def insert_heap(self,element):
#         self.length += 1
#         idx = self.length
#         self.arr[idx] = element
#         while True:
#             if idx == 1:
#                 break
#             else:
#                 parent_idx = idx//2
#                 if self.arr[idx]>self.arr[parent_idx]:
#                     self.arr[idx],self.arr[parent_idx]=self.arr[parent_idx],self.arr[idx]
#                     idx = parent_idx
#                 else:
#                     break
#     def delete_heap(self):
#         if self.length == 0:
#             return -1
#         pop_value = self.arr[1]
#         self.arr[1] = self.arr[self.length]
#         self.arr[self.length] = 0
#         self.length -= 1
#         idx = 1
#         while idx<self.length:
#             if self.arr[idx] < self.arr[idx*2] or self.arr[idx] < self.arr[idx*2+1]:
#                 if self.arr[idx*2] > self.arr[idx*2+1]:
#                     self.arr[idx],self.arr[idx*2]  = self.arr[idx*2] ,self.arr[idx]
#                     idx = idx*2
#                 else:
#                     self.arr[idx], self.arr[idx * 2 +1 ] = self.arr[idx * 2 + 1], self.arr[idx]
#                     idx= idx*2 + 1
#             else:
#                 break
#         return pop_value



# for t in range(1,int(input())+1):
#     N = int(input())
#     arr = ''
#     heap = Myheap(N)
#     for _ in range(N):
#         action = list(map(int,input().split()))
#         if action[0]==1:
#             heap.insert_heap(action[1])
#         else:
#             arr+=str(heap.delete_heap())+' '
#     print(f'#{t} {arr}')

def insert_heap(element):
    global length
    idx = length
    length += 1
    if idx == 1:
        heap[1] = element
        return
    else:
        heap[idx] = element
        while idx != 1: #부모 노드 = idx-1//2
            if heap[idx//2] < heap[idx]:
                heap[idx],heap[idx//2] = heap[idx//2],heap[idx]
                idx = idx//2
            else:return

def delete_heap():
    global length
    idx = length
    length -= 1

    if idx == 1:
        return '-1'
    else:
        tmp = 1
        pop_element = heap[tmp]

        heap[tmp],heap[idx] = heap[idx],heap[tmp]
        heap[idx] = 0
        while True:
            left_child = (tmp) * 2
            right_child = (tmp) * 2 + 1
            if left_child>length+1 or right_child > length+1:
                break
            if(heap[tmp] < heap[left_child]) or (heap[tmp] < heap[right_child]):
                if heap[left_child]<heap[right_child]:
                    heap[tmp],heap[right_child] = heap[right_child],heap[tmp]
                    tmp = right_child

                else:
                    heap[tmp], heap[left_child] = heap[left_child], heap[tmp]
                    tmp = left_child

            else:
                break

        return str(pop_element)

for t in range(1,int(input())+1):
    N = int(input())
    heap = [0] * (N+1)
    length = 1
    result = []
    action = [ list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        if action[i][0]==1:
            insert_heap(action[i][1])
        else:
            result.append(delete_heap())
    result = ' '.join(result)
    print(f'#{t} {result}')
