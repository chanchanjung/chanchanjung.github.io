import sys
from heapq import heappush, heappop
from collections import defaultdict


def dijkstra(graph, queue, distances, N, K):

    while queue:
        current_distance, current_node = heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for next_node in graph[current_node]:
            distance = current_distance + 1
            if distances[next_node] > distance:
                distances[next_node] = distance
                heappush(queue, (distance, next_node))

    answers = []
    for key, value in distances.items():
        if value == K:
            answers.append(key)
    return sorted(answers)


N, M, K, X = map(int, sys.stdin.readline().strip().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)


queue = []
heappush(queue, (0, X))
distances = {node: float('inf') for node in range(1, N+1)}
distances[X] = 0
answers = dijkstra(graph, queue, distances, N, K)
if answers:
    for answer in answers:
        print(answer)
else:
    print(-1)
