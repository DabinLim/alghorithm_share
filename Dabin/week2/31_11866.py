from collections import deque

n,k = map(int, input().split())

yose = deque()
result = []

for i in range(1,n+1):
    yose.append(i)

def moving(array):
    a = array.popleft()
    array.append(a)

print('<',end='')
while True:
    if len(yose) == 0:
        break

    for _ in range(k-1):
        moving(yose)
    print(yose.popleft(),end='')
    if yose:
        print(', ',end='')

print('>')
    