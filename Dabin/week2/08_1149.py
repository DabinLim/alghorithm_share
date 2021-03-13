n = int(input())
RGB =[]
for _ in range(n):
    RGB.append(list(map(int, input().split())))

for i in range(1, n):
    RGB_red_min = RGB[i][0] + min(RGB[i-1][1], RGB[i-1][2])          # i번째 집을 레드로 할 경우 i-1 번째 집을 어떤색으로 해야 가장 저렴할지 골라 미니멈 값 계산
    RGB[i][0] = RGB_red_min                                          # 1번째 집과 2번째 집을 칠하는 미니멈 값을 i번째에 저장하여 i+1번째 집을 칠할때 사용
    RGB_green_min = RGB[i][1] + min(RGB[i-1][0], RGB[i-1][2])        # i번째 집을 그린으로 할 경우 i-1 번째 집을 어떤색으로 해야 가장 저렴할지 골라 미니멈 값 계산
    RGB[i][1] = RGB_green_min                                        # 1번째 집과 2번째 집을 칠하는 미니멈 값을 i번째에 저장하여 i+1번째 집을 칠할때 사용
    RGB_blue_min = RGB[i][2] + min(RGB[i-1][0], RGB[i-1][1])         # i번째 집을 블루로 할 경우 i-1 번째 집을 어떤색으로 해야 가장 저렴할지 골라 미니멈 값 계산
    RGB[i][2] = RGB_blue_min                                         # 1번째 집과 2번째 집을 칠하는 미니멈 값을 i번째에 저장하여 i+1번째 집을 칠할때 사용

less_cost = min(RGB[n-1])                                            # n번째 집까지 칠하였을때의 미니멈 값
print(less_cost)