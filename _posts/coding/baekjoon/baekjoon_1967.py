import sys
from collections import defaultdict


N = int(sys.stdin.readline())
parents = [0 for _ in range(N)]
tree = defaultdict(dict)

for _ in range(N-1):
    parent, child, weight = map(int, sys.stdin.readline().strip().split())
    parents[parent-1] = 1
    tree[parent][child] = weight
    tree[child][parent] = weight

def bfs(tree, queue, visited):
    start = queue[0]
    while queue:
        now = queue.pop(0)
        if now in tree.keys():
            for key, value in tree[now].items():
                if key != start:
                    if visited[key-1] == 0:
                        visited[key-1] = visited[now-1] + value
                        queue.append(key)
    return max(visited)

answer = 0
for idx in range(1, N):
    if parents[idx] == 0:
        dimeter = bfs(tree, [idx+1], [0 for _ in range(N)])
        answer = max(dimeter, answer)
print(answer)



    