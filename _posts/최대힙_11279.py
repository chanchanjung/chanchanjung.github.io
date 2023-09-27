import sys
from heapq import heappush, heappop

queue = []

for _ in range(int(sys.stdin.readline().strip())):
    x = int(sys.stdin.readline().strip())

    if x == 0:
        if queue:
            print(heappop(queue)[1])
        else:
            print(0)
    else:
        heappush(queue, (-x, x))
