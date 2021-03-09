a, b = map(int, input().split())

def find_prime_list(number):
    for j in range(2, int(number**0.5) +1):
        if number % j == 0:
            return False

    return True

for i in range(a, b+1):
    if find_prime_list(i):
        print(i)