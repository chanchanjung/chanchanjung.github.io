import sys
from heapq import heappop, heappush


N = int(sys.stdin.readline())

rooms = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

change_rooms = [[float('inf') for _ in range(N)] for _ in range(N)]
change_rooms[0][0] = 0

queue = []
heappush(queue, (0, (0, 0)))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    current_break, current_node = heappop(queue)
    x, y = current_node
    if change_rooms[x][y] < current_break:
        continue

    for d in range(4):
        if -1 < x + dx[d] < N and -1 < y + dy[d] < N:
            breaks = current_break
            if rooms[x + dx[d]][y + dy[d]] == 0:
                breaks += 1
            if change_rooms[x + dx[d]][y + dy[d]] > breaks:
                change_rooms[x + dx[d]][y + dy[d]] = breaks
                heappush(queue, (breaks, (x + dx[d], y + dy[d])))

print(change_rooms[-1][-1])