x = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(x)]                  # dp[i]의 값을 1로 초기화

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:                 # 현재 위치(i)보다 이전에 있는 원소(j)가 작은지 확인 (크거나 같으면 가장 긴 증가하는 부분 수열이 될 수 없음)
            dp[i] = max(dp[i], dp[j]+1)     #작다면  현재 위치의 이전 숫자 중, dp 최댓값을 구하고 그 길이에 1을 더해주면 된다

print(max(dp))