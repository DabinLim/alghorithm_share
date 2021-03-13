import sys
from collections import deque

n = int(input())
command_list = []
for i in range(n):
    command_list.append(list(map(str, sys.stdin.readline().split())))

def stack(command, a):
    global stack_list

    if command == 'push':
        stack_list.appendleft(int(a))
        return stack_list
    elif command == 'top':
        if len(stack_list) == 0:
            return -1
        else:
            return stack_list[0]
    elif command == 'size':
        return len(stack_list)
    elif command == 'empty':
        if len(stack_list) == 0:
            return 1
        else:
            return 0
    elif command == 'pop':
        if len(stack_list) == 0:
            return -1
        else:
            return stack_list.popleft()


stack_list = deque()

for i in command_list:
    if len(i) > 1:
        stack(i[0],i[1])
    else:
        print(stack(i[0], 0))

