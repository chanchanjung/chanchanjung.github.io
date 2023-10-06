import sys
from heapq import heappop, heappush
from collections import defaultdict


def dijkstra(graph, distances, queue):

    while queue:
        current_distance, current_node = heappop(queue)

        if distances[current_node] < current_distance:
            continue
        
        for next_node, next_distance in graph[current_node].items():
            distance = current_distance + next_distance
            if distances[next_node] > distance:
                distances[next_node] = distance
                heappush(queue, (distance, next_node))
    return distances

N, E = map(int, sys.stdin.readline().strip().split())
graph = defaultdict(dict)
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = c
    graph[b][a] = c

node1, node2 = map(int, sys.stdin.readline().strip().split())

queue = []
heappush(queue, (0, 1))
start_distances = {node: float('inf') for node in range(1, N+1)}
start_distances[1] = 0
start_distances = dijkstra(graph, start_distances, queue)


queue = []
heappush(queue, (0, node1))
node1_distances = {node: float('inf') for node in range(1, N+1)}
node1_distances[node1] = 0
node1_distances = dijkstra(graph, node1_distances, queue)

queue = []
heappush(queue, (0, node2))
node2_distances = {node: float('inf') for node in range(1, N+1)}
node2_distances[node2] = 0
node2_distances = dijkstra(graph, node2_distances, queue)

answer = min(start_distances[node1] + node1_distances[node2] + node2_distances[N], start_distances[node2] + node2_distances[node1] + node1_distances[N])
if answer == float('inf'):
    print(-1)
else:
    print(answer)

