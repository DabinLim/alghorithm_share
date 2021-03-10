#6조 강상구의 코드
import sys 
from collections import deque

x_move = [0,0,-1,1]     #4방향 확인을 위해 설정함
y_move = [-1,1,0,0]

t_width,t_height = map(int, sys.stdin.readline().split());  #토마토 상자의 폭과 너비 ok
#토마토 정보를 받기
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(t_height)]; ok
start = []
temp_q = deque()  #popleft를 사용하기 위해 deque 사용
find_start(t_width,t_height,lines); #익은 토마토 위치 확인

#익은 토마토의 위치를 찾아 큐에 넣어주기
def find_start(t_width,t_height,lines):
    global temp_q
    for i in range(0,t_height):
        for j in range(0,t_width):
            if lines[i][j] == 1:                
                start= [i,j];
                temp_q.append(start);    
    return

#토마토가 익어 가는 함수
def go_tomato():        
    while temp_q: #큐에 익은 토마토 시작 지점이 없어질때까지 
        x,y = temp_q.popleft()        #토마토 위치 가져오기 
        for i in range(4):            #익은 토마토 위치 기준 4방향 확인
            next_x = x + x_move[i];                
            next_y = y + y_move[i];
               
            if 0<= next_x < t_height and 0<= next_y < t_width : #토마토 상자를 벗어나지 않아야함
                if lines[next_x][next_y] == 0 : #익지 않았으면 
                    lines[next_x][next_y] = lines[x][y] +1;   #영향을 준 토마토의 날짜에 1을 더해서 값을 변경
                    temp_q.append([next_x,next_y])       #이번에 익은 토마토의 위치를 큐에 저장
    return                     
       
x_move = [0,0,-1,1]     #4방향 확인을 위해 설정함
y_move = [-1,1,0,0]

t_width,t_height = map(int, sys.stdin.readline().split());  #토마토 상자의 폭과 너비
#토마토 정보를 받기
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(t_height)];
start = []
temp_q = deque()  #popleft를 사용하기 위해 deque 사용
find_start(t_width,t_height,lines); #익은 토마토 위치 확인
if temp_q == False :  #익은 토마토가 없으면 0을 출력
    print(0)
else : 
    go_tomato()  #토마토를 익히기
    day = max(map(max,lines)) -1   #첫날 익은 토마토의 시작 값이 1이었기때문에 제일 오래 걸린 날짜에서 -1 
    for i in range(0,t_height):    #익지 않은 토마토가 있으면 -1을 출력하고 종료
        for j in range(0,t_width):
            if lines[i][j] == 0:
                print(-1)
                exit()
    print(day)                     #모두 익었으면 걸린 날짜를 출력
