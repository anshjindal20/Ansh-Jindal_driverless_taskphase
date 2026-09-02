def distance(point, ref):
    x1, y1 = point
    x2, y2 = ref
    return (x1 - x2) ** 2 + (y1 - y2) ** 2
def sort_by_proximity(points, ref):
    n = len(points)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if distance(points[j], ref) < distance(points[min_index], ref):
                min_index = j

        points[i], points[min_index] = points[min_index], points[i]

    return points
n = int(input("Enter number of points: "))
points = []
for i in range(n):
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    points.append((x, y))
rx = int(input("Enter reference x coordinate: "))
ry = int(input("Enter reference y coordinate: "))
ref = (rx, ry)
print(sort_by_proximity(points, ref))