def hanoi(n, start, target, sub):
    if n ==1:
        print(start, target )
        return
    hanoi( n-1, start, sub, target)
    print(start, target)
    hanoi(n-1, sub, target, start)

n = int(input())
# N층짜리 하노이의 탑을 옮기려면 2^N - 1 번 옮겨야한다.
result = 1
for i in range(1, n+1):
    result = result * 2
print(result - 1)
hanoi(n, 1, 3, 2)

#input_num = int(input())
# def hanoi(num, start, middle, end):
#     if num == 0:
#         return
#     else:
#         (1번 재귀) hanoi(num-1, start, end, middle)
#         print(f"{start} 에서 {end} 여기로 옮겼다!")
#         (2번 재귀)hanoi(num-1, middle, start, end)
# sum = 0
# for i in range(input_num):
#     sum = sum * 2 + 1
# print(sum)
# hanoi(input_num, 1, 2, 3)
# hanoi(input_num, 1, 2, 3)
# 으로 함수를 호출하시면 작성하신 함수가 먼저 실행됩니다.이 함수를 0번 함수라 할게요.
# 0번 함수의 num값은 3 이기 때문에 return 되지 않고 1번 재귀를 만나 새로운 1번함수가 실행됩니다. 1번함수가 끝나기 전까지 0번함수는 중단된다고 생각해주세요.
# 1번 함수의 num도 2이기 때문에 리턴 되지 않고 다시 1번 재귀를 만나 새로운함수 2번함수가 실행됩니다.
# 2번함수가 진행되는 중에는 1번함수도 중단됩니다.
# 2번 함수의 num도 1이기 때문에 리턴 되지 않고 다시 1번 재귀를 만나 새로운 함수 3번함수가 실행 됩니다. 마찬가지로 2번 함수도 중단 됩니다.
# 3번 함수의 num은 0이기 때문에 리턴을 반환해주는데 여기서 3번함수는 끝이나고 2번함수로 되돌아갑니다.
# 아까 2번 함수는 1번재귀까지만 실행되고 중단 되었기 때문에 1번재귀 아래의 프린트문부터 다시 실행됩니다(1에서 3 여기로 옮겼다)
# 이후 2번 재귀를 만나 새로운 함수 4번 함수를 실행합니다 2번 함수의 num은 1 이었기 때문에 4번 함수의 num은 0이고 리턴을 반환합니다
# 다시 2번함수로 돌아왔지만 2번재귀까지 모두 실행해였으므로 2번함수는 끝이나고 1번함수로 돌아갑니다.
# 1번 함수 역시 1번재귀 까지만 실행 되고 중단 되었기 때문에 1번재귀 아래의 프린트문부터 실행 됩니다(1을 2 여기로 옮겼다.)
# 이런식으로 (i) 함수 내에서 (i+1)함수가 실행이  되고 (i+1) 함수 내에서 리턴되거나 함수가 끝이 나면 (i) 함수로 돌아간다고 생각해주시면 조금 더 이해하기 수월할것 같습니다.
# 석진님이 올려주신 영상도 같이 보시면 디버깅과 함께 설명 되어 있어 도움이 많이 될 것 같습니다.