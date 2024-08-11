n = int(input())
coords = []

for i in range(n):
    a,b = map(int,input().split())
    coords.append((a,b))

x_coords = [coord[0] for coord in coords]
y_coords = [coord[1] for coord in coords]

xmin = min(x_coords)
ymin = min(y_coords)
xmax = max(x_coords)
ymax = max(y_coords)

if n == 1:
    print(0)
else:
    print((xmax-xmin)*(ymax-ymin))