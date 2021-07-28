import sys

N = int(sys.stdin.readline())
points = dict()

for i in range(N):
    x, y = sys.stdin.readline().split('\n')[0].split(' ')
    x = int(x)
    y = int(y)

    if x not in points.keys():
        points[x] = list()
        points[x].append(y)
    else:
        points[x].append(y)

point_list = sorted(points.items(), key = lambda x : x[0])

for point in point_list:
    x = point[0]
    y_list = point[1]
    y_list.sort()
    for y in y_list:
        print(x, y)