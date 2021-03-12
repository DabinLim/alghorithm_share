n = int(input())
m = int(input())

graph = dict()  # 노드들의 인접 리스트를 저장할 공간       
virus_list = [] # 감염된 컴퓨터들을 저장할 공간

for i in range(1, n+1):  # 컴퓨터 수 만큼 빈 리스트 생성
    graph[i] = []

for i in range(m):       # 입력 받은 노드들의 인접 리스트 
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def infect_virus(ad_graph, virus_start):      # 시작 컴퓨터가 방문한 
    queue = [virus_start]                     # 컴퓨터는 모두 감염
    while queue:                            
        current_node = queue.pop()
        if current_node not in virus_list:
            virus_list.append(current_node)   # 방문한 컴퓨터 감염됨
        for ad_node in ad_graph[current_node]:
            if ad_node not in virus_list:
                queue.append(ad_node)         # 현재 컴퓨터의 인접 
    return                                    # 컴퓨터를 큐에 추가

infect_virus(graph, 1)
del virus_list[0]     # 바이러스 시작 컴퓨터를 제외
print(len(virus_list))
