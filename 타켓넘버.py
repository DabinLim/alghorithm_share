def solution(numbers, target):
    answer = 0
    
    def DFS(L,res):
        nonlocal answer
        if L==len(numbers):
            if res==target:
                answer+=1
            return
        DFS(L+1,res+numbers[L])
        DFS(L+1,res-numbers[L])
    DFS(0,0)
    print(answer)
    
    return answer