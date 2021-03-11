# case = int(input())

# for i in range(case):
#     n = int(input())
#     zero = 1
#     one = 0
#     for j in range(n):
#         temp = one
#         one = zero + one
#         zero = temp

#     print(zero,one)


#fibo(1) ,fibo(0) 의 출력 횟수

#fibo(0) -> 0,1번   1,0번
#fibo(1) -> 0,0번   1,1번
#fibo(2) -> fibo(1) + fibo(0)
#            0,1번    1,1번
#fibo(3) ->  fibo(2)  + fibo(1)    -> 0,1번 1,2번
#            0,1번 1,1번    1, 1번
#fibo(4) -> fibo(3) + fibo(2)
#           0,1반 1,2번    0,1번 1,1번  -> 0,2번  1,3번
#fibo(5) -> fibo(4) + fibo(3)
#           0,2번 1,3번 0,1번 1,2번  -> 0,3번   1,5번
#fibo(6) -> fibo(5) + fibo(4)
#           0,3번 1,5번   0,2번 1,3번   -> 0,5번   1,8번

# fibo(n-1)일떄 1이 나왔던 횟수만큼 fibo(n)에서 0이 나오고
# fibo(n-1)일떄 0과 1이 나온 횟수를 모두 더한 만큼 
# fibo(n) 에서 1이 나옴


memo = {
    0 : [1,0],   # fibo(0)일때 0 과 1 의 출력 횟수
    1 : [0,1]    # fibo(1)일때 0 과 1 의 출력 횟수
}

case = int(input())  

for _ in range(case):
    n = int(input())    
    for i in range(2, n+1):    # fibo(2) 이상인 경우 부터 계산
        memo[i] = [memo[i-1][1],memo[i-1][0]+memo[i-1][1]]
        # fibo(n)인 경우 memo안의 fibo(n-1)일떄 0과 1의 출력횟수 이용하여 fibo(n)일때 0과 1의 출력횟수 계산

    print(memo[n][0], memo[n][1])