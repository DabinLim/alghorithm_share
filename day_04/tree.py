# n, m = map(int, input().split())
# tree_list = list(map(int, input().split()))
# tree_list = sorted(tree_list)
# attempt_h = 0
# cut_tree_list = []
# for i in range(min(tree_list), max(tree_list) + m):  
#     del cut_tree_list[:]
#     for j in tree_list: 
#         if j - i > 0:
#             cut_tree_list.append(j-i)
#             if sum(cut_tree_list) >= m:
#                 attempt_h = i
        

# print(attempt_h)
import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
tree_list = Counter(map(int, sys.stdin.readline().split()))
start = 1
end = max(tree_list)
result = 0
while start <= end:
    mid = (start + end) // 2
    tree = 0
    for i in tree_list:
        if i > mid:
            tree += (i - mid) * tree_list[i]

    if tree >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

