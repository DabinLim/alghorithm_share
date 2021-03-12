from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()
for i in range(1, n+1):
    queue.append(i)


while True:
    if len(queue) == 1:
        break
    else:
        queue.popleft()
        temp = queue.popleft()    
        queue.append(temp)

print(queue[0])



# n = int(input())                    # 시간 초과
# queue = []
# for i in range(1, n+1):
#     queue.append(i)


# while True:
#     if len(queue) == 2:             # 1 2 3 4 5 6
#         break
#     else:
#         del queue[0]               # O(N) 의 시간 복잡도
#         temp = queue[0]             
#         del queue[0]               #  3 4 5 6 2 
#         queue.append(temp)

# print(queue[-1])
            
