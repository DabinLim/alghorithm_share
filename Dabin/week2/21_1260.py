n, m, v = map(int, input().split())

graph = dict()

for i in range(1,n+1):
    graph[i] = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i] = sorted(graph[i])

def dfs(ad_graph, start_number):
    stack = [start_number]
    visited = []

    while stack:
        current_number = stack.pop()
        if current_number not in visited:
            visited.append(current_number)
        for ad_number in reversed(ad_graph[current_number]):
            if ad_number not in visited:
                stack.append(ad_number)
    return visited


def bfs(ad_graph, start_number):
    queue = [start_number]
    visited = []

    while queue:
        current_number = queue.pop(0)
        if current_number not in visited:
            visited.append(current_number)
        for ad_number in ad_graph[current_number]:
            if ad_number not in visited:
                queue.append(ad_number)
    return visited

dfs_result = dfs(graph,v)
bfs_result = bfs(graph,v)

print(' '.join(str(i) for i in dfs_result))
print(' '.join(str(i) for i in bfs_result))