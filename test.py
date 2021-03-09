num = int(input())

def hanoi (n, f, t, o):
    if n == 1:
        print(f,t)
        return

    hanoi(n-1, f, o, t)
    print(f,t)
    hanoi(n-1, o, t, f)

hanoi(num,1,3,2)