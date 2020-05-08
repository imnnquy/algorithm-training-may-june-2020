# https://codeforces.com/problemset/problem/242/C


import heapq


class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist < other.dist


def dijkstra(start, end, allowed):
    dx = [-1, -1, -1, 1, 1, 1, 0, 0]
    dy = [-1, 0, 1, -1, 0, 1, 1, -1]

    dist = dict()
    pqueue = []
    heapq.heappush(pqueue, Node(start, 0))
    dist[start] = 0

    while len(pqueue) > 0:
        top = heapq.heappop(pqueue)
        u = top.id
        w = top.dist
        ux, uy = map(int, u.split('-'))
        for i in range(8):
            neighborx = ux + dx[i]
            neighbory = uy + dy[i]
            neighborid = f'{neighborx}-{neighbory}'
            if 10e9 > neighborx > 0 and 10e9 > neighbory > 0 and allowed.get(neighborid):
                if not dist.get(neighborid) or w + 1 < dist[neighborid]:
                    dist[neighborid] = w + 1
                    heapq.heappush(pqueue, Node(neighborid, dist[neighborid]))

    if dist.get(end):
        return dist[end]

    return -1


def solution():
    x0, y0, x1, y1 = map(int, input().strip().split())

    n = int(input())
    allowed = dict()

    for i in range(n):
        r, a, b = map(int, input().split())
        for j in range(a, b + 1):
            allowed[f'{r}-{j}'] = True

    print(dijkstra(f'{x0}-{y0}', f'{x1}-{y1}', allowed))


solution()
