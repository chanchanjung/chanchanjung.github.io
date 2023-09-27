import sys
from collections import defaultdict
from heapq import heappush, heappop


N = int(sys.stdin.readline().strip())

graph = defaultdict(list)

queue = []

start, end = map(int, sys.stdin.readline().strip().split())

m = int(sys.stdin.readline().strip())

for _ in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    graph[x].append(y)
    graph[y].append(x)

distances = {n: float('inf') for n in range(1, N+1)}
queue = []
heappush(queue, [0, start])

while queue:
    current_distance, now = heappop(queue)

    if distances[now] < current_distance:
        continue
    
    for member in graph[now]:
        distance = current_distance + 1
        if distance < distances[member]:
            distances[member] = distance
            heappush(queue, [distance, member])


if distances[end] == float('inf'):
    print(-1)
else:
    print(distances[end])