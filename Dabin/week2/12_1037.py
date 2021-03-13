import sys

n = int(sys.stdin.readline())
a_list = list(map(int, sys.stdin.readline().split()))
a1 = min(a_list)
a2 = max(a_list)
result = a1 * a2    # 1을 제외한 약수 최소값 * 약수 최대값 = 본인
print(result)
# a1 = max(a_list)
# a_list.remove(a1)
# a2 = max(a_list)
# max_com = 0
# for i in range(a1, a1*a2 + 1):
#     if a1 % i == 0 and a2 % i == 0:
#         max_com = i
#         break

# print(i)