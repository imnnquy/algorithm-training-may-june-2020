# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=22&page=show_problem&problem=2001


import heapq


class Meeting:
    def __init__(self, id, length):
        self.id = id
        self.length = length

    def __lt__(self, other):
        return self.length > other.length


def dfs(graph, result, start, times, visited):
    if visited[start]:
        return
    visited[start] = True
    for u in graph[start]:
        if not visited[u]:
            dfs(graph, result, u, times, visited)

    result.append(len(result) + times[start])


def solution():
    n = int(input())
    times = [0 for i in range(n)]
    graph = [[] for i in range(n)]
    queue = []
    for i in range(n):
        lines = list(map(int, input().split()))
        times[i] = lines[0]
        for j in range(2, lines[1] + 2):
            graph[i].append(lines[j] - 1)
        heapq.heappush(queue, Meeting(i, times[i]))

    result = []
    visited = [False for i in range(n)]
    while queue:
        dfs(graph, result, heapq.heappop(queue).id, times, visited)

    longest = 0
    for i in range(n):
        if result[i] > longest:
            longest = result[i]
    print(longest)


solution()
