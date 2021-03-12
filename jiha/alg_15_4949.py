while True:
    stack=[];push,pop=stack.append,stack.pop
    s=input()
    if s=='.':break                                     #.입력 종료조건
    r='yes'
    for c in s:
        if c in ['[','(']:                              #열린 부호면 받아주고
            push(c)                                     #push로 추가
        elif c==']':
            if not stack or pop()!='[':r='no';break     #종류 일치 여부 판단
        elif c==')':
            if not stack or pop()!='(':r='no';break
    if stack:r='no'                                     #하나라도 일치하지 않으면 'no'
    print(r)