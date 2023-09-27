import sys
from collections import deque

queue = deque()

for _ in range(int(sys.stdin.readline().strip())):
    commands = list(map(int, sys.stdin.readline().strip().split()))
    if commands[0] == 1:
        queue.appendleft(commands[1])
    elif commands[0] == 2:
        queue.append(commands[1])
    elif commands[0] == 3:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif commands[0] == 4:
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif commands[0] == 5:
        print(len(queue))
    elif commands[0] == 6:
        if queue:
            print(0)
        else:
            print(1)
    elif commands[0] == 7:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif commands[0] == 8:
        if queue:
            print(queue[-1])
        else:
            print(-1)

