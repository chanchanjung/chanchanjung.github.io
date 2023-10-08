import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().strip().split())
name_dict = defaultdict(bool)
for _ in range(N):
    name_dict[sys.stdin.readline().strip()] = 1
answer = []
for _ in range(M):
    no_watcher = sys.stdin.readline().strip()
    if name_dict[no_watcher] == 1:
        answer.append(no_watcher)
print(len(answer))
for name in sorted(answer):
    print(name)