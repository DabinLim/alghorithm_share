import math

case = int(input())

for i in range(case):
    a, b = map(int, input().split())
    gcd = math.gcd(a,b)
    result = a * b // gcd
    print(result)