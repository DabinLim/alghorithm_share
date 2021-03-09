a=list(input().upper())    #upper = 대문자로 변경하는 함수
b=[]
c=[]
d=65
e=0
for i in range(65,91): #아스키 코드
    b.append(i) #위치 참고 용
    c.append(i)  #각 알파벳이 등장하는 횟수를 저장하는 배열

for i in a:
    c[b.index(ord(i))]+=1 #등장횟수 저장 (아스키코드값에 누적) <-> chr

for i in c:
    c[e]=i-d  # 누적된 값을 빼주기
    d=d+1
    e=e+1

if c.count(max(c))>1: # 최대등장횟수가 겹칠때
   print("?")
else:
   print(chr(b[c.index(max(c))])) #C에서 최대등장횟수의 알파벳 위치 B로 반환후 변환해서 출력