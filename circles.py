import math
import random
from drawtool import DrawTool

dt = DrawTool()

dt.set_XY_range(0,10, 0,10)

# Change to circles1.txt and later to circles2 and circles3.txt
filename = 'circles3.txt'

does_overlap = []
originX = []
originY = []
radius = []

num_circles = 0

def read_circles(filename):
    radius, originX, originY = [],[],[]
    num_circles = 0
    with open(filename,'r') as in_file:
        line = in_file.readline()
        n = int(line.strip())
        num_circles = n
        for i in range(n):
            # Read each circle
            line = in_file.readline()
            data = line.split()
            originX.append(float(data[0].strip()))
            originY.append(float(data[1].strip()))
            radius.append(float(data[2].strip()))
    return num_circles, originX, originY, radius

def print_circles():
    print('Number of circles =', num_circles)
    for i in range(num_circles):
        print('origin x =', originX[i],
            'origin y =', originY[i], 
            ' radius =', radius[i])

def overlap(o1x, o1y, r1, o2x, o2y, r2):
    """
    return true if the circle(o1x, o1y, r1) overlap with circle(o2x, o2y, r2) else return false
    """
    # write your code here
    # check to see if two circles overlap
    # the circles will have origins o1x, o1y and o2x, o2y
    # and radii r1 and r2
    # return true if they overlap
    # else return false
    distance_between_circles = math.sqrt((o1x - o2x)**2 + (o1y - o2y)**2)
    sum_of_radious = r1 + r2
    if distance_between_circles > sum_of_radious:
        return False
    return True

def check_overlaps(originX, originY, radius):
    does_overlap = [False for _ in range(num_circles)]
    # write your code here
    # does_overlap is a list of booleans
    # with length equal to the number of circles
    # it starts with each value as false
    # use nested loops to change the value of
    # does_overlap for each circle
    # changing it to true if the circle overlaps any other circle

    for x in range(num_circles):
        for y in range(num_circles):
            if overlap(originX[x],originY[x],radius[x],originX[y],originY[y],radius[y]) and x != y:
                does_overlap[x] = True
    return does_overlap


num_circles, originX, originY, radius = read_circles(filename)
print_circles()
does_overlap = check_overlaps(originX, originY, radius)

# Draw in two colors
for i in range(num_circles):
    color = 'b'
    if does_overlap[i]:
        color = 'r'
    dt.set_color(color)
    dt.draw_circle(originX[i], originY[i], radius[i])

dt.display()