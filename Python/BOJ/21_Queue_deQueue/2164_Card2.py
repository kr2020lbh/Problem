def enQueue(item):
    cards.append(item)


def deQueue():
    global start
    item = cards[start]
    start+=1
    return item

N = int(input())
cards = [ i for i in range(1,N+1)]
start = 0

for i in range(N-1):
    deQueue()
    enQueue(deQueue())
print(cards[start])
