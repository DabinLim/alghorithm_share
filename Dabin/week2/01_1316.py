n = int(input())
word_list = []
count = 0
for i in range(n):                      # n 개의 단어를 받음
    word_list = []                      # 케이스마다 리스트 초기화
    word = input()
    for j in word:                      # 단어 글자 하나하나 돌면서          
        if j not in word_list:          # 처음 들어오는 글자면 추가
            word_list.append(j)
        elif j == word_list[-1]:        # 처음 들어오는 단어는 아니지만 연속된 글자면 추가
            word_list.append(j)
        else:                           # 처음도 아니고 연속된 것도 아닌 글자면 잘못된글자
            word_list.append('wrong') 
    if 'wrong' not in word_list:        # 잘못된 글자가 포함되지 않았다면 그룹단어임 그러므로 그룹단어 갯수 1개 추가
        count += 1


print(count) # 그룹단어 갯수 출력