# https://codeforces.com/problemset/problem/337/D


import heapq


def dfs(graph, start):
    n = len(graph)
    dist = [-0 for i in range(n + 1)]
    visited = [False for i in range(n + 1)]
    visited[start] = True
    stack = []
    dist[start] = 0
    heapq.heappush(stack, start)

    while stack:

        u = heapq.heappop(stack)

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                heapq.heappush(stack, v)

    return dist


def solution():
    n, m, d = map(int, input().strip().split())
    p = list(map(int, input().strip().split()))
    graph = [[] for i in range(n + 1)]
    for i in range(n - 1):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    dist = dfs(graph, 1)

    max_distance = -1
    u = -1
    v = -1
    for i in p:
        if dist[i] > max_distance:
            max_distance = dist[i]
            u = i

    distu = dfs(graph, u)

    max_distance = -1
    for i in p:
        if distu[i] > max_distance:
            max_distance = distu[i]
            v = i

    distv = dfs(graph, v)

    affected = 0

    for i in range(1, n + 1):
        if 0 <= distu[i] <= d and 0 <= distv[i] <= d:
            affected += 1

    print(affected)


solution()
