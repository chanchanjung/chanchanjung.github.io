import sys

N, M = map(int, sys.stdin.readline().strip().split())

poketmons = dict()

for idx in range(1, N+1):
    name = sys.stdin.readline().strip()
    poketmons[str(idx)] = name
    poketmons[name.lower()] = idx

for _ in range(M):
    print(poketmons[sys.stdin.readline().strip().lower()])

