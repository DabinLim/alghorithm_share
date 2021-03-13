n = int(input())

for _ in range(n):
    stack = []
    result = True
    string = str(input())
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')' and len(stack) != 0:
            if stack[-1] == '(':
                stack.pop()
        else:
            result = False
    
    if result and not stack:
        print('YES')
    else:
        print('NO')