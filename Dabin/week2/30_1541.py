sik = input().split('-')
sum_sik = 0
if len(sik) == 1:
    for i in sik[0].split('+'):
        sum_sik += int(i)
else:
    for i in sik[0].split('+'):
        sum_sik += int(i)
        
    for i in sik[1:]:
        for j in i.split('+'):
            sum_sik -= int(j)

print(sum_sik)