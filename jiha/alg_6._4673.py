
#n = a+10*b+100*c
#n_t = n+a+b+c
#while True:
  #  if b==0, c==0:
  #  elif c==0:
  # else:
  #      print(n)
setA = {i for i in range(1, 10001)} #집합 for 셀프넘버 setA에 입력
setB = set()                        #set(중복 삭제)  for X 셀프넘버for i in range(1, 10001):
for i in range(1, 10001):
    for j in str(i):
        i += int(j)                 #셀프넘버 찾기
    setB.add(i)                     #셀프넘버 setB에 추가

setA = sorted(setA-setB)            #순서 정열 - (딕셔너리도 받을 수 있음)
for i in setA:
    print(i)

