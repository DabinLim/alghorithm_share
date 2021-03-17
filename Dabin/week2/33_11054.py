n = int(input())

subseq = list(map(int, input().split()))

count_f = [1]*n

for i in range(n):
    for j in range(i):
        if subseq[i] > subseq[j]:
            count_f[i] = max(count_f[i],count_f[j]+1)


subseq_b = list(reversed(subseq))
count = [1]*n

for i in range(n):
    for j in range(i):
        if subseq_b[i] > subseq_b[j]:
            count[i] = max(count[i],count[j]+1)

count_b = list(reversed(count))

result = []
for i in range(n):
    result.append(count_f[i] + count_b[i] - 1)

