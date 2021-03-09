import string
word=input()

croa=['c=','c-','dz=','d-','lj','nj','s=','z=']
a=word                                              #입력값 사용
cnt=0                                               #결과값
for i in range(0,len(croa)):
    if str(croa[i]) in word:
        g=str(croa[i])
        cnt=cnt+(a.count(g))                        #입력값 결과값에 삽입
        a=a.replace(g,'#')                          #인식 위해 문자열 치환
for i in list(string.ascii_lowercase):              #소문자만을 포함하는 문자열 / 대,소문자는 string.ascii_letters
    cnt=cnt+a.count(i)
print(cnt)