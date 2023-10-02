import sys

string = sys.stdin.readline().strip()

N = int(sys.stdin.readline().strip())

cursor = len(string)

for _ in range(N):
    commands = list(sys.stdin.readline().strip().split())

    if commands[0] == 'L':
        if cursor > 0:
            cursor -= 1
    elif commands[0] == 'D':
        if cursor < len(string):
            cursor += 1
    elif commands[0] == 'P':
        if cursor == len(string):
            string = string + commands[1]
            cursor += 1
        elif cursor == 0:
            string = commands[1] + string
            cursor += 1
        else:
            string = string[:cursor] + commands[1] + string[cursor:]
            cursor += 1
    elif commands[0] == 'B':
        if cursor == len(string):
            string = string[:-1]
            cursor -= 1
        elif cursor > 0:
            string = string[:cursor-1] + string[cursor:]
            cursor -= 1
print(string)



