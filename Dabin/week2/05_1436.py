n = int(input())

name = 666
count = 0
while True:
    if '666' in str(name):
        count += 1
        if n == count:
            print(name)
            break
    name += 1
