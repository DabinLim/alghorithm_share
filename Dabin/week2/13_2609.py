import sys
import math

a, b = map(int, sys.stdin.readline().split())

min = math.gcd(a,b)           # math 모듈의 gcd(최소공약수) 사용방식
max = a * b // min
print(min)
print(max)


# min_max_com_list = []
# for i in range(b + 1, 1, -1):                # 각각 for문을 돌려서 구하는 방식 (미친짓)
#     if a % i == 0 and b % i == 0:
#         min_max_com_list.append(i)
#         break

# for j in range(a+1 , a*b+1):
#     if j % a == 0 and j % b == 0:
#         min_max_com_list.append(j)
#         break

# for l in min_max_com_list:
#     print(l)

    # def uc(x,y):              # 유클리드 호제법 사용방식
#     while(y): 
#         x,y = y, x%y
#     return x

# min = uc(b,a)