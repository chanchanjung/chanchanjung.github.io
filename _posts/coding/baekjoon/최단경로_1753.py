import sys
import heapq
from collections import defaultdict

V, E = map(int, sys.stdin.readline().strip().split())

start = int(sys.stdin.readline().strip())


answer = [-1 for _ in range(V)]
answer[start-1] = 0

graph = defaultdict(dict)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    if u in graph:
        if v in graph[u]:
            if graph[u][v] > w:
                graph[u][v] = w
        else:
            graph[u][v] = w
    else:
        graph[u] = {v: w}


def dijkstra(graph, start):
    distances = {v: float('INF') for v in range(1, V+1)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances

for value in dijkstra(graph, start).values():
    if value == float('INF'):
        print("INF")
    else:
        print(value)
