num = int(input())

display = []
for _ in range(num):
    display.append(list(map(int, input().split())))

def separate(x,y,n):

    if n == 1:
        return str(display[x][y]) 

    compression = []  
    for i in range(x, x+n):
        for j in range(y, y+n):
            if display[i][j] != display[x][y]:

                compression.append('(')
                compression.extend(separate(x, y, n//2))
                compression.extend(separate(x, y + n//2, n//2))
                compression.extend(separate(x + n//2, y, n//2))
                compression.extend(separate(x + n//2, y + n//2, n//2))
                compression.append(')')
                return compression
    return str(display[x][y])


print(''.join(separate(0,0,num)))


