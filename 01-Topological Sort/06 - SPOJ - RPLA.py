# https://www.spoj.com/problems/RPLA/


import heapq


def kahn(graph):
    V = len(graph)
    in_degree = [0] * V
    for i in range(V):
        for j in graph[i]:
            in_degree[j] += 1
    zero_in_degree = []
    ranks = [[] for i in range(V)]
    people_ranking = [0 for i in range(V)]
    for i in range(V):
        if in_degree[i] == 0:
            zero_in_degree.append(i)
            heapq.heappush(ranks[0], i)
            people_ranking[i] = 0

    result = []

    while zero_in_degree:
        u = zero_in_degree.pop(0)

        result.append(u + 1)
        for i in graph[u]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                zero_in_degree.append(i)
                people_ranking[i] = people_ranking[u] + 1
                heapq.heappush(ranks[people_ranking[i]], i)
    return ranks


def solution():
    T = int(input())
    for t in range(T):
        N, R = map(int, input().split())
        graph = [[] for i in range(N)]
        for i in range(R):
            r1, r2 = map(int, input().split())
            graph[r2].append(r1)

        result = kahn(graph)

        print(f'Scenario #{t + 1}:')
        for i in range(N):
            if not result[i]:
                break
            while result[i]:
                print(f'{i + 1} {heapq.heappop(result[i])}')


solution()
