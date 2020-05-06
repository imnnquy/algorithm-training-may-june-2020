# https://vn.spoj.com/problems/MAKETREE/


def kahn(graph):
	V = len(graph)
	in_degree = [0] * V
	for i in range(V):
		for j in graph[i]:
			in_degree[j] += 1
	zero_in_degree = []
	for i in range(V):
		if in_degree[i] == 0:
			zero_in_degree.append(i)
	result = []

	while zero_in_degree:
		u = zero_in_degree.pop(0)

		result.append(u + 1)
		for i in graph[u]:
			in_degree[i] -= 1
			if in_degree[i] == 0:
				zero_in_degree.append(i)

	mapping_result = [0 for i in range(V)]
	for i in range(1, V):
		mapping_result[result[i] - 1] = result[i - 1]

	return mapping_result


def solution():
	N, K = map(int, input().split())
	graph = [[] for i in range(N)]
	for i in range(K):
		lines = list(map(int, input().split()))
		length = len(lines)
		for j in range(1, length):
			graph[i].append(lines[j] - 1)

	result = kahn(graph)

	print(*result, sep='\n')


solution()
