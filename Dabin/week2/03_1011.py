import math

case = int(input())
for _ in range(case):
    start, end = map(int, input().split())
    dis= end - start                             # 시작점과 끝점의 거리
    moving = math.ceil(dis/math.floor((dis ** 0.5))) + (math.floor((dis**0.5)) - 1 )  # 시작점과 끝점간의 거리(dis) 를 거리의 제곱근의 자연수 부분으로 나눈 뒤에 올림을 해준다.
    print(moving)                                                                     # 그 값에 거리의 제곱근의 자연수 부분 에 -1을 한 값을 더해 주면 이동거리가 나온다.