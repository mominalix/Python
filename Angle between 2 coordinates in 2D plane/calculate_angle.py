import math


def calculate_angle(point1, point2):
    p1 = (0, 0)
    # p2 is now a vector from point1 to point2
    p2 = (point2[0]-point1[0], point2[1]-point1[1])
    # The math.atan2() method returns a numeric value between -π and π representing the angle theta of an (x, y) point.
    ang1 = math.atan2(p1[1], p1[0])
    ang2 = math.atan2(p2[1], p2[0])
    angle = ((ang2 - ang1) * (180.0 / 3.141592653589793))
    # Return only positive angle
    if angle < 0:
        angle += 360
    print(angle)
    return angle


Point1 = []
Point2 = []

Point1.append(int(input("First point x: ")))
Point1.append(int(input("First point y: ")))
Point2.append(int(input("Second point x: ")))
Point2.append(int(input("Second point y: ")))

print("Angle between points = "+str(calculate_angle(Point1,Point2)))