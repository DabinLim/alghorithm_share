import sys

n = int(sys.stdin.readline())
color_papers = []
for i in range(n):
    color_papers.append(list(map(int, sys.stdin.readline().split())))

blue = 0
white = 0

def separate(x, y, n):
    global blue, white

    check = color_papers[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != color_papers[i][j]:
                
                separate(x, y, n//2)
                separate(x, y + n//2, n//2)
                separate(x + n//2, y, n//2)
                separate(x + n//2, y + n//2, n//2)
                return

    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return

separate(0,0,n)
print(white)
print(blue)
