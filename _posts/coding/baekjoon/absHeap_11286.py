import sys
import heapq

N = int(sys.stdin.readline().strip())

queue = []

for _ in range(N):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        if not queue:
            print(0)
        else:
            print(heapq.heappop(queue)[1])
    else:
        heapq.heappush(queue, (abs(n), n))
