count = 0
count_list = []
def solution(begin, target, words):
    if target not in words:
        return 0
    begin = list(begin)
    target = list(target)
    def dfs(Lv, begin, target, words):
        global count, count_list
        if begin == target:
            count_list.append(count)
            return 
        if Lv == len(words):
            return
        b_target_cnt = 0
        w_target_cnt = 0
        diff_cnt = 0
        for i in begin:
            for j in target:
                if i == j:
                    b_target_cnt += 1
        for i in words[Lv]:
            for j in target:
                if i == j:
                    w_target_cnt += 1
        for i in range(len(begin)):
            if begin[i] != words[Lv][i]:
                diff_cnt += 1
                    
        if w_target_cnt > b_target_cnt and diff_cnt < 2:
            for i in target:
                if i in word[Lv] and i not in begin:
                    begin[target.index(i)] = target[target.index(i)]
                    count += 1
                    dfs(Lv+1, begin, target, words)
                    break
        elif w_target_cnt == b_target_cnt:
            dfs(Lv+1, begin, target, words)
            for i in words[Lv]:
                if i != begin[words[Lv].index(i)]:
                    begin[words[Lv].index(i)] =words[Lv][words[Lv].index(i)]
                    count += 1
                    dfs(Lv+1, begin, target, words)
                    count -= 1
                    break
        else:
            dfs(Lv+1, begin, target, words)
        
            
    dfs(0,begin,target,words)
    if len(count_list) < 1:
        answer = 0
    else:
        answer = min(count_list)
    return answer