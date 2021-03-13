n, k = map(int, input().split())

coin_list = []

for _ in range(n):
    a = int(input())
    coin_list.append(a)

coin_list = sorted(coin_list, reverse=True)

count = 0

for i in coin_list:
    count += k // i
    k %= i

print(count)