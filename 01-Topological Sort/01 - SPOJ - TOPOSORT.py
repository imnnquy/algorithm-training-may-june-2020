#https://www.spoj.com/problems/TOPOSORT/
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
		
		result.append(u + 1)
		for i in graph[u]:
			in_degree[i] -= 1
			if in_degree[i] == 0:
				heapq.heappush(zero_in_degree, i)
	return result

def solution():
	V, E = map(int, input().split())
	graph = [[] for i in range(V)]
	for i in range(E):
		u, v = map(int, input().split())
		graph[u - 1].append(v - 1)

	result = kahn(graph)
	if len(result) < V:
		print('Sandro fails.')
	else:
		print(*result)

solution()
