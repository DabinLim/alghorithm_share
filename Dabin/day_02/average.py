# %.3f 

c = int(input())

for i in range(c):
    x = list(map(int, input().split()))
    student = x[0]
    avg = (sum(x[1:])) / (len(x) -1)
    grade = x[1:]
    honor = []
    for j in grade:
        if j > avg:
            honor.append(j)
    honor_rate = (len(honor) / student) * 100
    print('%.3f'%honor_rate+'%')
# print 할때 fstring
    