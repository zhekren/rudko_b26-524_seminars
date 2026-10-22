def dist(point1, point2):
    return ((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)**0.5

def func(list, control_point):
    mini = 99999999999
    dot_x = None
    for i in range(len(list)):
        if dist(list[i], control_point) < mini:
            mini = dist(list[i], control_point)
            dot_x = list[i]
    return dot_x, mini

print(func([(1,2), (2,3), (3,4)], (1000, -500)))