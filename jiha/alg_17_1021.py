import sys

N, M = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split(' ')))
queue = [i for i in range(1, N + 1)]          #자연수들의 queue 생성

ans = 0
for target in targets:
    plus_index = queue.index(target)          #1. 앞에꺼를 뒤로 넘기는 연산 수
    minus_index = len(queue) - plus_index     #2. 뒤에꺼를 앞으로 넘기는 연산 수
    steps = min(plus_index, minus_index)      # 둘 중 최솟값

    # plus는 1번 연산
    # minus는 2번 연산
    if steps == plus_index:
        sign = 'plus'
    else:
        sign = 'minus'

    if sign == 'plus':
        for _ in range(steps):
            temp = queue.pop(0)
            queue.append(temp)        #뒤로 삽입
    else:
        for _ in range(steps):
            temp = queue.pop(-1)
            queue.insert(0, temp)   # 앞으로 데이터 삽입

    ans += steps
    queue.pop(0)            

print(ans)