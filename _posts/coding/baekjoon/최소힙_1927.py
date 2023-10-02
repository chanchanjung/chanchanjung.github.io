import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().strip())

queue = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())

    if x == 0:
        if queue:
            print(heappop(queue))
        else:
            print(0)
    else:
        heappush(queue, x)

