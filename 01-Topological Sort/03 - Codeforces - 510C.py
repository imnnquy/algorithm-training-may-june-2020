# https://codeforces.com/problemset/problem/510/C


import heapq


def kahn(graph):
    V = len(graph)
    in_degree = [0] * V
    for i in range(V):
        for j in graph[i]:
            in_degree[j] += 1
    zero_in_degree = []
    for i in range(V):
        if in_degree[i] == 0:
            heapq.heappush(zero_in_degree, i)
    result = []

    while zero_in_degree:
        u = heapq.heappop(zero_in_degree)

        result.append(chr(u + 97))
        for i in graph[u]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                heapq.heappush(zero_in_degree, i)
    return result


def solution():
    V = 26
    E = int(input())
    graph = [[] for i in range(V)]
    names = []
    for i in range(E):
        names.append(input().strip())

    for i in range(E - 1):
        min_length = min(len(names[i]), len(names[i + 1]))
        found = False
        for j in range(min_length):
            if names[i][j] != names[i + 1][j]:
                found = True
                graph[ord(names[i][j]) - 97].append(ord(names[i + 1][j]) - 97)
                break
        if not found and len(names[i]) > len(names[i + 1]):
            print('Impossible')
            return

    result = kahn(graph)
    if len(result) < V:
        print('Impossible')
    else:
        print(*result, sep='')


solution()
