# H : 층수,  W: 방 수, N: 몇번째 손님인지
# H * W
# N // H
# N % H

# for i in range (1 ,H):
# H, W, N = map(int,input().split())
# result1 = (N % H)
# result2 = (N//H) +1
# t = 0
# if result2 <10:
#     result2 = str(t)+result2
# print(str(result1)+str(result2))

     # N % H  //  N // H + 1
# 테스트케이스 입력받기
t = int(input())

for i in range(t):
    # h,w,n 입력받기
    h, w, n = map(int, input().split())

    # 호수 구하기
    line = n // h + 1
    # 사람수가 층수로 나누어질때
    if n % h == 0:
        floor = h
        line = n // h
    else:
        floor = n % h

    answer = floor * 100 + line  # pow(10, 2)
    print(answer)