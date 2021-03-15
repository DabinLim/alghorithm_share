import sys
import statistics
from collections import Counter

n = int(sys.stdin.readline())

num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

def find_average(num_list):
    num_1 = round(sum(num_list)/n)
    return num_1

def find_median(num_list):
    num_2 = statistics.median(num_list)
    return num_2

def find_mode(num_list):
    num_list.sort()
    counted = Counter(num_list).most_common()
    if len(counted) > 1:
        if counted[0][1] == counted[1][1]:
            return counted[1][0]
    else:
        return counted[0][0]
    

def find_range(num_list):
    num_3 = max(num_list) - min(num_list)
    return num_3

print(find_average(num_list))
print(find_median(num_list))
print(find_mode(num_list))
print(find_range(num_list))


