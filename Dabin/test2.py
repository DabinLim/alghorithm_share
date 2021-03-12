N = 123456 * 2 + 1
prime_list = [True] * N
for i in range(2, int(N**0.5)+1):
    if prime_list[i]:
        for j in range(2*i, N, i):
            prime_list[j] = False

while True:
    n = int(input())
    count = 0
    if n == 0:
        break
    if n == 1:
        print(1)
    else:
        for i in range(n + 1, 2*n):
            if prime_list[i]:
                count +=1
        print(count)