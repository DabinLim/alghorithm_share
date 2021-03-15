# n = int(input())

# score_list = []
# max_list = []

# for _ in range(n):
#     score_list.append(int(input()))

# score_list.reverse()

# max_list.append(score_list[0])
# del score_list[0]

# count = 0

# while True:
#     if len(score_list) <= 2:
#         break
#     first_max = max(score_list[0],score_list[1])
#     total_max = max(score_list[2],first_max)
#     if first_max > score_list[2] and count <= 2:
#         max_list.append(total_max)
#         if score_list[1] > score_list[0]:
#             del score_list[0]
#             del score_list[0]
#         else:
#             count += 1
#             del score_list[0]
#     elif first_max > score_list[2] and count > 2:
#         if score_list[1] > score_list[2]:
#             max_list.append(score_list[1])
#             del score_list[0]
#             del score_list[0]
#         else:
#             max_list.append(score_list[2])
#         del score_list[0]
#         del score_list[0]
#         del score_list[0]

#     else:
#         max_list.append(score_list[2])
#         del score_list[0]
#         del score_list[0]
#         del score_list[0]

# if len(score_list) == 2:
#     max_list.append(max(score_list[0],score_list[1]))
# elif len(max_list) == 1:
#     max_list = max_list
# else:
#     max_list.append(score_list[0])

# print(sum(max_list))

n = int(input())
score_list = []
dp = []
for _ in range(n):
    score_list.append(int(input())) 
if n == 1:
    dp.append(score_list[0])
elif n == 2:
    dp.append(score_list[0]+score_list[1])
elif n == 3:
    dp.append(max(score_list[0]+score_list[2],score_list[1]+score_list[2]))

else:   
    dp.append(score_list[0])
    dp.append(score_list[0]+score_list[1])
    dp.append(max(score_list[0]+score_list[2],score_list[1]+score_list[2]))

    for i in range(3,n):
        dp.append(max(score_list[i]+score_list[i-1]+dp[i-3],score_list[i]+dp[i-2]))

print(dp.pop())