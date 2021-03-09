n = int(input())
stack = []
pm_list = []
count = 1
possible = True
for i in range(n):
    target = int(input())
    while count <= target:
        stack.append(count)
        pm_list.append('+')
        count+=1
    if stack[-1] == target:
        stack.pop()
        pm_list.append('-')
    else:
        possible = False
if possible == False:
    print('NO')
else:
    for i in pm_list:
        print(i)

