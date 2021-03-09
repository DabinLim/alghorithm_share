# A = 올라간 거리 / B = 밤에 내려간 거리 / V (높이) = A - B / D = 소요일수
import sys
import math
a,b,v = map(int, sys.stdin.readline().split())
print(math.ceil((v-a)/ (a-b)) +1)