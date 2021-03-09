while True:
    sentence = input()
    if sentence == '.':
        break
    stack = []
    result = True
    
    for i in sentence:
        if i == '[' or i =='(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                result = False
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                result = False
                break
        elif i == ']':
            if len(stack) == 0:
                result = False
                break
            elif stack[-1] == '[':
                stack.pop()
            else:
                result = False
                break

    if result and not stack:
        print('yes')
    else:
        print('no')




            


