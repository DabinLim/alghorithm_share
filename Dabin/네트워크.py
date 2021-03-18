from collections import deque

def solution(n, computers):
    graph = dict()
    for i in range(n):
        graph[i] = []
        
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
    def find_start():
        graph_key = list(graph.keys())
        if len(graph_key) < 1:
            start_node = 'x'
        else:    
            start_node = graph_key[0]
        return start_node
    
    def bfs(ad_graph, start_node):
        queue = [start_node]
        visited = []
        if start_node == 'x':
            visited.append('x')
            return visited
        while queue:
            current_node = queue.pop(0)
            if current_node not in visited:
                visited.append(current_node)
            for ad_node in ad_graph[current_node]:
                if ad_node not in visited:
                    queue.append(ad_node)
                    
        return visited
    
    count = 0
    while True:
        start_node = find_start()
        visited = bfs(graph,start_node)
        if visited[0] == 'x':
            break
        for i in visited:
            del graph[i]
        count += 1
    
    answer = count 
    
    return answer