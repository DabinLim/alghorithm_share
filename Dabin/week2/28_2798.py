n, m = map(int, input().split())
card_list = list(map(int, input().split()))
card_list.sort()

three_list = []
cards = []
for i in range(n):
    for j in range(1, n):
        for l in range(2, n):
            if i < j  and j < l:
                cards = [card_list[i],card_list[j],card_list[l]]
                three_list.append(cards)


sum_list = []
for i in three_list:
    if sum(i) <= m:
        sum_list.append(sum(i))

print(max(sum_list))
