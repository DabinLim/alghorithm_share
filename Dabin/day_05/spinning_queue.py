# def spinning_queue(target_number) :
#     if target_number <= len(queue)//2 -1:
#         moving_queue = queue[0]
#         del queue[0]
#         queue.append(moving_queue)
#     else:
#         moving_queue = queue[-1]
#         del queue[-1]
#         queue.insert(0, moving_queue)
#     return queue


n, m = map(int, input().split())
target_list = list(map(int, input().split()))
count = 0
queue = []

for i in range(1, n+1):
    queue.append(i)

def spinning_left():
    moving_queue = queue[0]
    del queue[0]
    queue.append(moving_queue)

    return 

def spinning_right():
    moving_queue = queue[-1]
    del queue[-1]
    queue.insert(0, moving_queue)
    return 

for target_number in target_list:
    while True:                                         # target_number 가 아닌 queue.index(target_number) 인 이유는
        if queue.index(target_number) <= len(queue)//2: # 큐는 계속 회전하기 때문에 현재 target_number의 위치를 구해야 어떤 방향이 연산이 더 적게 필요한지 알 수 있음
                spinning_left()                         # index를 구하는데 추가로 -1을 하지 않는 이유는 
            if queue[0] != target_number:               # 삭제하려면 0번쨰 index까지 돌려야 하기 때문에 1번의 연산이 더 필요함
                count += 1
            else:
                del queue[0]
                break
        else:
            if queue[0] != target_number:
                spinning_right()
                count += 1
            else:
                del queue[0]
                break

print(count)
# print (queue)
# # target_number = list(map(int, input().split()))
# target_number = 5

# if target_number <=
# queue[4] 까지는 왼쪽으로 이동
# queue[5] 부터는 오른쪽으로 이동
