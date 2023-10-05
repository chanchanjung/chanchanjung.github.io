import sys
from heapq import heappop, heappush
from collections import defaultdict


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = defaultdict(dict)
for _ in range(m):
    start, end, weight = map(int, sys.stdin.readline().strip().split())
    if end not in graph[start].keys():
        graph[start][end] = weight
    elif graph[start][end] > weight:
        graph[start][end] = weight
start, end = map(int, sys.stdin.readline().strip().split())

costs = {node: float('inf') for node in range(1, n+1)}
costs[start] = 0
queue = []
heappush(queue, (0, start, [start]))
end_visited = []

while queue:
    current_cost, current_node, visited = heappop(queue)
    if costs[current_node] < current_cost:
        continue

    for next_node, next_cost in graph[current_node].items():
        cost = current_cost + next_cost
        if costs[next_node] > cost:
            if next_node == end:
                end_visited = visited + [next_node]
            costs[next_node] = cost
            heappush(queue, (cost, next_node, visited + [next_node]))

print(costs[end])
print(len(end_visited))
print(*end_visited)