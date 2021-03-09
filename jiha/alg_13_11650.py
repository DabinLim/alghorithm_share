n=int(input())
coordinate=[]                             # (x,y) 들어올떄마다 저장

for _ in range(n):
    (x,y)= list(map(int,input().split()))
    coordinate.append((x,y))

sorted_coordinate=sorted(coordinate)         # sorted함수 적용 (정렬의 새로운 리스트 반환)

for i in sorted_coordinate:                  # 원소 하나씩 프린트
    print(i[0], i[1])