import sys

N = int(sys.stdin.readline())
points = dict()
for i in range(N):
    x, y = sys.stdin.readline().split('\n')[0].split(' ')
    x = int(x)
    y = int(y)
    if y not in points.keys():
        points[y] = list()
        points[y].append(x)
    else:
        points[y].append(x)

point_list = sorted(points.items(), key = lambda y: y[0])

for point in point_list:
    x_list = point[1]
    y = point[0]

    x_list.sort()

    for x in x_list:
        print(x, y)