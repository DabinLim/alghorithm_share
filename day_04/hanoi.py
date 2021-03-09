num = int(input())
move_list = []
def hanoi (n, f, t, o):
    if n == 1:
        move_list.append([f,t])
        return
    hanoi(n -1 , f, o, t)
    move_list.append([f,t])
    hanoi(n-1, o, t, f)

hanoi(num,1,3,2)
print(len(move_list))
for i in move_list:
    print(i[0], i[1])