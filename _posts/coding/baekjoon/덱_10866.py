import sys
from collections import deque

queue = deque()

for _ in range(int(sys.stdin.readline().strip())):
    commands = list(sys.stdin.readline().strip().split())
    
    if commands[0] == 'push_back':
        queue.append(int(commands[1]))
    elif commands[0] == 'push_front':
        queue.appendleft(int(commands[1]))
    elif commands[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif commands[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif commands[0] == 'size':
        print(len(queue))
    elif commands[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif commands[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif commands[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)