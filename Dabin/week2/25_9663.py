import sys

n = int(sys.stdin.readline().split()[0])

# 쉬운 이해 : 각각 대각선마다 번호를 지정해줄 경우 col-row+(n-1)을 하면 왼쪽 대각선 번호 col+row를 하면 오른쪽 대각선 번호를 구할 수 있다.
#           퀸을 둘때 대각선 번호를 True로 지정해준다음 새로 두는 퀸의 대각선 번호가 이미 True인 경우 그 위치에 둘 수 없음

flag_Row = [False] * n      # 같은 직선 상의 있을 경우의 수 = n
flag_Ldig = [False] * ((n * 2) - 1) # 대각선 상에 있을 경우의 수 (n*2)-1
flag_Rdig = [False] * ((n * 2) - 1) # 대각선 상에 있을 경우의 수 (n*2)-1
cnt = 0
def alg(col) :
    global cnt
    for row in range(n) :       # 1부터 n까지 돌면서
        if flag_Row[row] == False and flag_Ldig[col - row + (n - 1)] == False and flag_Rdig[col + row] == False :       
            # 이 위치에 두어도 직선 and 왼쪽 대각선 and 오른쪽 대각선의 퀸들로부터 죽지 않는다면 퀸을 둔다
            if col == n - 1 :                   # 만약 n번까지 다 두었다면
                cnt += 1                        # 총 경우의 수 1 증가
                return
            else :                              # 아직 n번째 줄까지 돌지 않았다면
                flag_Row[row] = True                      # 방금 둔 위치의 직선 방향은 둘 수 없게   (row)
                flag_Ldig[col - row + (n - 1)] = True     # 방금 둔 위치가 다음 퀸의 왼쪽 대각에 있을 경우의 수 모두 x
                                                          #(col-row의 값이 같으면 같은 대각선상에 위치, col-row가 0보다 작은 경우를 대비해 n-1 값을 더해줌 왜냐하면 col-row의 최저값은 0-(n-1))
                flag_Rdig[col + row] = True               # 방금 둔 위치가 다음 퀸의 오른쪽 대각에 있을 경우의 수도 모두 x (col과 row의 합이 같으면 같은 대각선상에 위치)
                alg(col + 1)                              # 다음 퀸의 위치를 정하기 위해 함수 호출
                flag_Row[row] = False                     # 다음 퀸을 둘 수 있는 경우의 수가 없다면 돌아와 방금 
                flag_Ldig[col - row + (n - 1)] = False    # 둔 퀸은 회수 하여야 하므로 못 두는 경우의 수 모두 해제
                flag_Rdig[col + row] = False               

alg(0)  # 첫줄부터 어디에 두어야 할지 검사, 첫줄에 n까지 돌아도 경우의 수가 없다면 count = 0
print(cnt)