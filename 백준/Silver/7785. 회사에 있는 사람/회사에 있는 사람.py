import sys
input = sys.stdin.read

data = input().splitlines()

n = int(data[0])

people_inside = set()

for i in range(1, n + 1):
    line = data[i]
    name, status = line.split()

    if status == 'enter':
        people_inside.add(name)
    elif status == 'leave':
        if name in people_inside:
            people_inside.remove(name)


people_inside = sorted(people_inside, reverse=True)

for x in people_inside:
    print(x)