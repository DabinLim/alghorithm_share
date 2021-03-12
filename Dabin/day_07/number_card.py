import sys
n1 = int(input())
m1 = set(map(int, sys.stdin.readline().split()))
n2 = int(input())
m2 = set(map(int, sys.stdin.readline().split()))
result = []
for i in m2:
    if i in m1:
        result.append('1')
    else:
        result.append('0')

print(' '.join(result))