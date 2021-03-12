def count_fibonacci(n):
    zero_count = [1,0]              #한발느린 피보나치?!         # f(0)호출 횟수
    one_count = [0,1]                                           # f(1)호출 횟수
    if n <= 1:
        return
 
    for i in range(2, n+1):                                     #피보나치 공식
        zero_count.append(zero_count[i-1] + zero_count[i-2])
        one_count.append(one_count[i-1] + one_count[i-2])
 
    return zero_count, one_count
 
n = int(input())                                                #피보나치 함수 크기 지정
zero_count, one_count = count_fibonacci(40)
 
for _ in range(n):
    m = int(input())                                            #각 테스트 케이스 입력
    print(zero_count[m], one_count[m])              #정수형 변환/ 출력