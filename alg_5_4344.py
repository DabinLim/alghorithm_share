import sys
n = int(input())
for i in range(n):
    lst = list(map(int, sys.stdin.readline().strip().split()))  #input으로 받으면 시간초과 일어날 수 있음  [sys , readline()] 사용, 1000개는 괜찮긴함
    avg = sum(lst[1:])/lst[0]
    cnt = 0
    for score in lst[1:]:                                       #학생 순회하며 cnt+1씩 증가
        if score > avg:
            cnt +=1
    print('%.3f%%' % (cnt/lst[0]*100))                          # %두개 입력