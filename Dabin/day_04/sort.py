# 직접 구현한 삽입 정렬

dot = int(input())
dots = []
for i in range(dot):
    dot_location = list(map(int, input().split()))
    dots.append(dot_location)
    
n = len(dots)
for i in range(1, n):
    for j in range(i):
        if dots[i - j - 1][1] > dots[i - j][1]:
            dots[i - j -1] , dots [i - j] = dots [i - j], dots[i - j -1]
        elif dots[i - j - 1][1] == dots[i - j][1]:
            if dots[i - j -1][0] > dots[i - j][0]:
                dots[i - j -1] , dots [i - j] = dots [i - j] , dots[i - j -1]
        else:
            break

for i in range(len(dots)):
    print(dots[i][0], dots[i][1])


# 람다 함수를 이용한 2차원 리스트 정렬

dot = int(input())
dots = []

for i in range(dot):
    [a,b] = list(map(int, input().split()))
    dots.append([a, b])

dots = sorted(dots, key = lambda x : x[1])

for i in range(len(dots)):
    print(dots[i][0], dots[i][1])

# x 축과 y 축의 위치를 바꾸어 정렬한 후 반대로 출력 

dot = int(input())
dots = []

for i in range(dot):
    [a,b] = list(map(int, input().split()))
    dots.append([b, a])

dots = sorted(dots)
for i in range(len(dots)):
    print(dots[i][1], dots[i][0])
