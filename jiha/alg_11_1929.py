def isPrime(num):             #소수인지 검사해주는 함수
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):        # 런타임 때문에 제곱근 까지만 검사 ( num * num < k)
            if num % i == 0:
                return False
        return True


M, N = map(int, input().split())      # 정답 열 나열

for i in range(M, N + 1):
    if isPrime(i):
        print(i)
