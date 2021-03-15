case = int(input())
for _ in range(case):
    points = list(map(int, input().split()))
    sum_radius = points[2] + points[5]
    if points[5] > points[2]:
        sub_radius = points[5] - points[2]
    elif points[5] < points[2]:
        sub_radius = points[2] - points[5]
    else:
        sub_radius = 0
    point_dis = (((points[3]-points[0])**2) + ((points[4]-points[1])**2))**0.5         # ((x2-x1)^2 + (y2-y1)^2) ** 0.5
    if points[0] == points[3] and points[1] == points[4]:     #(x1 == x2 and y1 == y2)  원이 중심이 같을때
        if points[2] == points[5]:                            # r1 == r2                원의 반지름 또한 같다면 접점은 무한대 반지름이 다르다면 접점은 없음
            print(-1)                                                                   
        else:
            print(0)                                                                    
    elif sum_radius > point_dis and sub_radius < point_dis:         # 두 원이 교차 하는 경우
        print(2)
    elif sum_radius == point_dis or sub_radius == point_dis:        # 두 원이 외접 하거나 내접 하는 경우
        print(1)
    elif sum_radius < point_dis or sub_radius > point_dis:          # 두 원이 떨어져 있거나 한원 안에 다른 원이 들어가 있는 경우
        print(0)