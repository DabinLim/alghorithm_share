from collections import deque

n = int(input())
houses = [list(input()) for _ in range(n)]

visited = [[0]*n for _ in range(n)]

queue = deque()
move_x = [0,0,-1,1]    
move_y = [-1,1,0,0]

def find_start():
    start = []
    for i in range(n):
        if len(start) > 0:
            break
        for j in range(n):
            if houses[i][j] != '0' and visited[i][j] == 0:
                start = [i,j]
                queue.append(start)
                break
    return start

for l in range(1,n):
    start = [find_start()]
    if len(start) == 0:
        exit()

    while queue:
        x,y = queue.popleft()
        for j in range(4):
            next_x = x + move_x[j]
            next_y = y + move_y[j]
            if 0 <= next_x < n and 0 <= next_y < n:
                if houses[next_x][next_y] != '0' and visited[next_x][next_y]== 0:
                    visited[next_x][next_y] += l

                    queue.append([next_x,next_y])


count_list = dict()
for i in range(1,n+1):
    count_list[i] = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] != 0:
            count_list[visited[i][j]] += 1

result = []

for i in range(1,n+1):
    if count_list[i] != 0:
        result.append(count_list[i])

print(len(result))
for i in sorted(result):
    print(i)