import sys
from heapq import heappush, heappop
from collections import defaultdict

N, M, X = map(int, sys.stdin.readline().strip().split())

times = {node: float('inf') for node in range(1, N+1)}
reverse_times = {node: float('inf') for node in range(1, N+1)}
answer = 0

graph = defaultdict(dict)
reverse_graph = defaultdict(dict)

for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().strip().split())
    graph[start][end] = weight
    reverse_graph[end][start] = weight


queue = []
heappush(queue, (0, X))
times[X] = 0
while queue:
    time, now = heappop(queue)

    if times[now] < time:
        continue
    
    for new_node, add_time in graph[now].items():
        next_time = time + add_time
        if next_time < times[new_node]:
            times[new_node] = next_time
            heappush(queue, (next_time, new_node))

queue = []
heappush(queue, (0, X))
reverse_times[X] = 0
while queue:
    time, now = heappop(queue)

    if reverse_times[now] < time:
        continue
    
    for new_node, add_time in reverse_graph[now].items():
        next_time = time + add_time
        if next_time < reverse_times[new_node]:
            reverse_times[new_node] = next_time
            heappush(queue, (next_time, new_node))

for i in range(1, N+1):
    answer = max(answer, times[i] + reverse_times[i])

print(answer)