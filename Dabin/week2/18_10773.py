import sys
from collections import deque

n = int(sys.stdin.readline())

stack = deque()

for _ in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        stack.appendleft(a)
    else:
        stack.popleft()
result = 0
for i in stack:
    result += i
print(result)
