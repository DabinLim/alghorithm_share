# import sys

# n, m = map(int, sys.stdin.readline().split())

# check_list = [False] * n

# arr = []

# def dfs(count):
#     if count == m:                       # 길이 m의 수열이 완성 될 경우 프린트
#         print(*arr)
#         return

#     for i in range(0,n):
#         if(check_list[i]):               # 방문한 숫자(이미 배열에 들어가 있거나 출력된 숫자)
#             continue    

#         check_list[i] = True             # 방문한 숫자인지 확인
#         arr.append(i+1)                  # 방문하지 않은 경우 배열에 숫자 추가
#         dfs(count+1)                     # 출력 완료 후 함수 종료 및 수열 마지막 숫자 빼기
#         arr.pop()

#         for j in range(i+1, n):          # 처음 호출된 함수 (첫번째 숫자) 체크 리스트
#             check_list[j] = False

# dfs(0)

import itertools

n, m = map(int, input().split())

result = itertools.combinations(range(1,n+1),m)
for i in result:
    print(*i)