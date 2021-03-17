import sys 
import operator 
N = int(sys.stdin.readline()) 
arr = list(map(int, sys.stdin.readline().split())) 
inc = [1] * N 
dec = [1] * N 
for i in range(N): 
    for j in range(i): 
        if arr[i] > arr[j] and inc[i] <= inc[j]: 
            inc[i] = inc[j] + 1 

for i in range(N-1, -1, -1): 
    for j in range(i, N): 
        if arr[i] > arr[j] and dec[i] <= dec[j]: 
            dec[i] = dec[j] + 1 
            
print(inc,dec)

sys.stdout.write(str(max(map(operator.add, inc, dec)) - 1))

