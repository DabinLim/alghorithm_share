n = int(input())
triangle = []
for _ in range(n):
    a = list(map(int, input().split()))
    triangle.append(a)


for i in range(n-1, 0, -1):           # 가장 아랫 줄 가장 오른쪽부터 반복
    for j in range( n):
        if i - j < 1 :
            break
        maxi = triangle[i-1][i-j-1] + max(triangle[i][i-j], triangle[i][i-j-1])    # 가장 아랫 줄 가장 오른쪽부터 그 왼쪽 숫자와 비교하여 큰 수를 윗줄 숫자와 더한다.
        triangle[i-1][i-j-1] = maxi                                                # 더한 값으로 대체한다. (총 최댓값을 구하기 위해)

print(triangle[0][0])  # 더하고 더해 결국 맨 윗줄의 숫자를 구한다 (최댓값들만 골라서 더한 값)



# for i in range(n-1, 0, -1):
#     max_a = triangle[i-1][i-1] + max(triangle[i][i], triangle[i][i-1])
#     triangle[i-1][i-1] = max_a
#     max_b = triangle[i-1][i-2] + max(triangle[i][i-1], triangle[i][i-2])
#     triangle[i-1][i-2] = max_b
#     max_c = triangle[i-1][i-3] + max(triangle[i][i-2], triangle[i][i-3])
#     triangle[i-1][i-3] = max_c
#     max_d = triangle[i-1][i-4] + max(triangle[i][i-3], triangle[i][i-4])
#     triangle[i-1][i-4] = max_d