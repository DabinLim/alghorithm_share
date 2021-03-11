# num = int(input())
# sequence = list(map(int, input().split()))
# count = 1
# result = [min(sequence)]
# for i in range(len(sequence)):
#     if i == len(sequence) - 1:
#         break
#     if sequence[i]<sequence[i+1]:
#         result.append(sequence[i+1])

# print(len(result))
    

n = int(input())
sequence = list(map(int, input().split()))

count = [1]*n
for i in range(n):
    for j in range(i):
        if sequence[i] > sequence[j] and count[j] >= count[i]:
            count[i] += 1
print(max(count))

# print(max(count))