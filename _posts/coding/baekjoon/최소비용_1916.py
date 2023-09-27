import sys
from heapq import heappush, heappop
from collections import defaultdict


N = int(sys.stdin.readline().strip())

M = int(sys.stdin.readline().strip())

graph = defaultdict(dict)

for _ in range(M):
    s_bus, e_bus, cost = map(int, sys.stdin.readline().strip().split())
    if s_bus in graph.keys():
        if e_bus in graph[s_bus].keys():
            if graph[s_bus][e_bus] > cost:
                graph[s_bus][e_bus] = cost
        else:
            graph[s_bus][e_bus] = cost
    else:
        graph[s_bus] = {e_bus: cost}

start, end = map(int, sys.stdin.readline().strip().split())

queue = []

heappush(queue, (0, start))

arrived = {n: float('inf') for n in range(1, N+1)}

while queue:
    cost, now = heappop(queue)
    if arrived[now] < cost:
        continue
    
    for bus, add_cost in graph[now].items():
        new_cost = cost + add_cost
        if new_cost < arrived[bus]:
            arrived[bus] = new_cost
            heappush(queue, (new_cost, bus))
print(arrived[end])
