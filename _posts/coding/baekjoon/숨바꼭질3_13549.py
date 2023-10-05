import sys
from heapq import heappop, heappush

N, K = map(int, sys.stdin.readline().strip().split())

queue = []
visited = dict()
if N == K:
    print(0)
else:
    heappush(queue, (0, N))


    while queue:
        time, now = heappop(queue)

        if now -1 > -1:
            if (now-1) not in visited.keys() or visited[now - 1] > time + 1:
                heappush(queue, (time + 1, now - 1))
                visited[now-1] = time + 1
        if now < K:
            if now + 1 <= 100000:
                if (now+1) not in visited.keys() or visited[now + 1] > time + 1:
                    heappush(queue, (time + 1, now + 1))
                    visited[now+1] = time + 1
            if now * 2 <= 100000 and now < K:
                if (now*2) not in visited.keys() or visited[now * 2] > time:
                    heappush(queue, (time, now * 2))
                    visited[now*2] = time

    print(visited[K])

        

