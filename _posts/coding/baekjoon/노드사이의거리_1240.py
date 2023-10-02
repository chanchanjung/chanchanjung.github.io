import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().strip().split())
nodes  = defaultdict(dict)
for _ in range(N-1):
    node1, node2, weight = map(int, sys.stdin.readline().strip().split())
    if node2 not in nodes[node1].keys():
        nodes[node1][node2] = weight
    if node1 not in nodes[node2].keys():
        nodes[node2][node1] = weight

for _ in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    visited = [0 for _ in range(N)]
    queue = [start]    
    while visited[end-1] == 0:
        now = queue.pop()
        for key, value in nodes[now].items():
            if visited[key-1] == 0:
                visited[key-1] = visited[now-1] + value
                queue.append(key)
    print(visited[end-1])


