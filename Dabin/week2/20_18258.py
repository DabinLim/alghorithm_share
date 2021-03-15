import sys
from collections import deque

n = int(input())

def queue(command, a):
    global queue_list

    if command == 'push':
        queue_list.append(int(a))
        return queue_list
    elif command == 'front':
        if len(queue_list) == 0:
            return -1
        else:
            return queue_list[0]
    elif command == 'back':
        if len(queue_list) == 0:
            return -1
        else:
            return queue_list[-1]

    elif command == 'size':
        return len(queue_list)

    elif command == 'empty':
        if len(queue_list) == 0:
            return 1
        else:
            return 0
    elif command == 'pop':
        if len(queue_list) == 0:
            return -1
        else:
            return queue_list.popleft()

queue_list = deque()

for i in range(n):         
    a = list(sys.stdin.readline().split())
    if len(a) > 1:
        queue(a[0],a[1])
    else:
        print(queue(a[0], 0))


