
case = int(input())

for i in range(case):
    h,w,n = map(int, input().split())
    floor = n%h
    line = n//h +1
    if n % h == 0:
        floor = h
        line = n//h
    match_room =floor * 100 + line
    print(match_room)
# for i in match_room:
#     print(i)

