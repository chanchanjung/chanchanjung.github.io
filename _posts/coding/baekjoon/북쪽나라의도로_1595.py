import sys
from collections import defaultdict, deque
cities = set()
loads = defaultdict(dict)
while True:
    try:
        city1, city2, load = map(int, sys.stdin.readline().strip().split())
        cities.add(city1)
        cities.add(city2)
        loads[city1][city2] = load
        loads[city2][city1] = load
    except:
        break

answer = 0
def bfs(loads,city):
    max_distance = 0
    queue = deque()
    queue.append(([city], 0))
    while queue:
        cities, distance = queue.pop()
        addDistance = False
        for next_city, load in loads[cities[-1]].items():
            if next_city not in cities:
                addDistance = True
                queue.append((cities + [next_city], distance + load))
        if not addDistance:
            if max_distance < distance:
                max_distance = distance
    return max_distance


for city in cities:
    distance = bfs(loads, city)
    if answer < distance:
        answer = distance

print(answer)


