import sys
from heapq import heappop, heappush



def dijkstra(idx, N):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    crave = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    moneys = [[float('inf') for _ in range(N)] for _ in range(N)]
    moneys[0][0] = crave[0][0]
    queue = []
    heappush(queue, (crave[0][0], (0, 0)))

    while queue:
        current_money, current_node = heappop(queue)
        x, y = current_node
        for d in range(4):
            if -1 < x + dx[d] < N and -1 < y + dy[d] < N:
                money = current_money + crave[x + dx[d]][y + dy[d]]
                if moneys[x + dx[d]][y + dy[d]] > money:
                    moneys[x + dx[d]][y + dy[d]] = money
                    heappush(queue, (moneys[x + dx[d]][y + dy[d]], (x + dx[d], y + dy[d])))
    print(f"Problem {idx}: {moneys[-1][-1]}")



idx = 1
while True:
    N = int(sys.stdin.readline().strip())
    if N == 0:
        break

    dijkstra(idx, N)
    idx += 1