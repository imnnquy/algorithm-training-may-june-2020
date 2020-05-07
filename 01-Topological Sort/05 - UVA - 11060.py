# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=22&page=show_problem&problem=2001


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

        result.append(u)
        for i in graph[u]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                heapq.heappush(zero_in_degree, i)
    return result


def solution():
    counter = 1
    while True:
        N = 0
        try:
            N = int(input())
        except Exception:
            return
        name_to_order = dict()
        order_to_name = ['' for i in range(N)]

        for i in range(N):
            name = input().strip()
            name_to_order[name] = i
            order_to_name[i] = name

        graph = [[] for i in range(N)]
        M = int(input())
        for i in range(M):
            first, seccond = map(str, input().split())
            graph[name_to_order[first]].append(name_to_order[seccond])

        result = kahn(graph)
        map_result = []
        for i in range(N):
            map_result.append(order_to_name[result[i]])

        print(f'Case #{counter}: Dilbert should drink beverages in this order: ', end='')
        print(*map_result, end='.')
        counter += 1

        try:
            input()
        except Exception:
            return

        print()


solution()
