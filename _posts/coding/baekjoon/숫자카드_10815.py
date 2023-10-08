import sys
from collections import defaultdict

sys.stdin.readline()
cards = defaultdict(int)

for num in list(map(int, sys.stdin.readline().strip().split())):
    cards[num] = 1

sys.stdin.readline()
answer = []
for num in list(map(int, sys.stdin.readline().strip().split())):
    answer.append(cards[num])

print(*answer)
