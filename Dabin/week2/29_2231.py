n = int(input())

S_list = []

for i in range(1, n+1):
    sum_i = 0
    for j in str(i):
        sum_i += int(j)
    result = i +sum_i
    if result == n:
        S_list.append(i)
        break
if len(S_list) == 0:
    print(0)
else:    
    print(S_list[0])
        