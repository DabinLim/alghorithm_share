import sys
from collections import deque

box_w, box_h = map(int, sys.stdin.readline().split())

tomatos = []
for i in range(box_h):
    tomatos.append(list(map(int, sys.stdin.readline().split())))
# tomatos = [list(map(int, sys.stdin.readline().split())) for _ in range(box_h)]
start = []
queue = deque()
x_move = [0,0,-1,1]     #4방향 확인을 위해 설정함
y_move = [-1,1,0,0]

def find_start(box_w, box_h, tomatos):
    for i in range(box_h):
        for j in range(box_w):
            if tomatos[i][j] == 1:
                start = [i,j]
                queue.append(start)
    return

find_start(box_w, box_h, tomatos)


def ripe_tomato():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x = x + x_move[i]
            next_y = y + y_move[i]

            if 0<= next_x < box_h and 0<= next_y <box_w:
                if tomatos[next_x][next_y] == 0:
                    tomatos[next_x][next_y] = tomatos[x][y] +1;
                    
                    queue.append([next_x,next_y])
    return

not_riped_count = 0

for i in range(box_h):
        for j in range(box_w):
            if tomatos[i][j] == 0:
                not_riped_count += 1

if not_riped_count == 0:
    print(0)
else:
    ripe_tomato()
    day = max(map(max, tomatos)) -1

    for i in range(box_h):
        for j in range(box_w):
            if tomatos[i][j] == 0:
                print(-1)
                exit()
    print(day)
                