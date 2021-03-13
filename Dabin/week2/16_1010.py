from math import factorial as f

case = int(input())
for i in range(case):
    k,n = map(int, input().split())
    if k < 0 or k > n:
        print(0)
    else:
        print(int(f(n) / ( f(k) * f(n-k) ) ))