# #힙
import sys
sys.stdin = open("input.txt","r")


class Heap:
    heap_length = 0
    
    def __init__(self):
        self.arr = [0] * N

    def insert(self,n):
        tmp_idx = self.heap_length
        if self.heap_length == 0:
            self.arr[self.heap_length]=n

        else:
            self.arr[self.heap_length] = n
            while tmp_idx > 0:
                parent_idx = (tmp_idx-1)//2
                if self.arr[parent_idx]<self.arr[tmp_idx]:
                    self.arr[parent_idx],self.arr[tmp_idx] = self.arr[tmp_idx],self.arr[parent_idx]
                    tmp_idx = parent_idx
                else:
                    break

        self.heap_length += 1

    def delete(self):
        if self.heap_length == 0:
            return -1

        elif self.heap_length == 1:
            result = self.arr[0]
            self.arr[0] = 0

        else:
            result = self.arr[0]
            self.arr[0],self.arr[self.heap_length-1]=self.arr[self.heap_length-1],self.arr[0]
            self.arr[self.heap_length-1] = 0


            parent_idx = 0
            left_child_idx = parent_idx*2+1
            right_child_idx = parent_idx*2+2

            while self.arr[left_child_idx] !=0 or self.arr[right_child_idx] !=0 :
                if self.arr[parent_idx] < self.arr[left_child_idx] or self.arr[parent_idx] < self.arr[right_child_idx]:
                    if self.arr[left_child_idx] >= self.arr[right_child_idx]:
                        self.arr[parent_idx],self.arr[left_child_idx] = self.arr[left_child_idx],self.arr[parent_idx]
                        parent_idx = left_child_idx
                    else:
                        self.arr[parent_idx],self.arr[right_child_idx] = self.arr[right_child_idx],self.arr[parent_idx]
                        parent_idx = right_child_idx

                    left_child_idx = parent_idx*2+1
                    right_child_idx = parent_idx*2+2
                else:
                    break
        self.heap_length -= 1
        return result

for t in range(1,int(input())+1):
    N = int(input())
    myheap = Heap()

    commands = [ list(map(int,input().split())) for _ in range(N) ]

    print(f'#{t}', end=' ')
    for command in commands:
        if command[0] == 1:
            myheap.insert(command[1])
        elif command[0] == 2:
            print(myheap.delete(),end=' ')
    print()

