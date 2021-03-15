import sys
from collections import deque

n = int(sys.stdin.readline())
queue_list = deque()

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue_list.append(int(command[1]))

    elif command[0] == 'front':
        if len(queue_list) == 0:
            print(-1) 
        else:
            print(queue_list[0])

    elif command[0] == 'back':
        if len(queue_list) == 0:
            print(-1)
        else:
            print(queue_list[-1])

    elif command == 'size':
        print(len(queue_list))

    elif command == 'empty':
        if len(queue_list) == 0:
            print(1) 
        else:
            print(0) 
    elif command == 'pop':
        if len(queue_list) == 0:
            print(-1) 
        else:
            print(queue_list.popleft())


