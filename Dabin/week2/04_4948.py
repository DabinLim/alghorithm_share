





while True:
    n = int(input())
    if n == 0:
        break
    prime_list = []
    if n == 1:
        print(1)
    else:
        for i in range(n + 1 , 2*n):
            if i == 1:
                prime_list.append(1)
                break
            test = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    test = False
            if test:
                prime_list.append(i)
        print(len(prime_list))
        



            

