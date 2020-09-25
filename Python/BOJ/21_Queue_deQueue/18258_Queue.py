import sys
sys.stdin = open("input.txt","r")
'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

def push(X):
    global last
    Q.append(X)
    last += 1


def pop():
    global first
    global last
    if first == last:return -1
    first += 1
    return Q[first]


def size():
    return last - first


def empty():
    if first == last: return 1
    return 0


def front():
    if first == last:return -1
    return Q[first + 1]


def back():
    if first == last: return -1
    return Q[last]


N = int(sys.stdin.readline())
Q = []
first = last = -1
for i in range(N):
    commands = sys.stdin.readline().split()
    param = commands[0]
    if param == 'push':push(commands[1])
    elif param == 'pop':print(pop())
    elif param == 'size':print(size())
    elif param == 'empty':print(empty())
    elif param == 'front':print(front())
    elif param == 'back':print(back())


