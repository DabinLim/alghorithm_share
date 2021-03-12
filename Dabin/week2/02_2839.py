z = int(input())
correct_list = []
for i in range(z//5 +1):       # 5 * i 가 z를 넘어간다면 검사할 필요가 없음
    for j in range(z//3 + 1):      # 3 * i 가 z를 넘어간다면 검사할 필요가 없음
        if 5*i + 3*j ==  z:         # 5i + 3j 가 z 로 맞아 떨어진다면
            correct_list.append(i+j) # 그래서 총 몇 봉투 인지 저장

if correct_list == []:       # 맞아떨어지지 않는다면 저장된 봉투수 없음
    print(-1)
else:                       
    print(min(correct_list))   # 맞아떨어진 봉투 수 중에 가장 적은 봉투 수