import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
answer = 'Yes'
queue = deque()




nodes = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    nodes[a].append(b)

bear_count = int(sys.stdin.readline().strip())
bears = list(map(int, sys.stdin.readline().strip().split()))

if 1 not in bears:
    queue.append(1)

while queue:
    no = queue.popleft()
    if not nodes[no]:
        answer = 'yes'
        break
    
    for node in nodes[no]:
        if node not in bears:
            queue.append(node)
print(answer)



