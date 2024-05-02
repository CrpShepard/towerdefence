import math

def normalized_xy(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    distance = math.sqrt(dx**2 + dy**2)

    normalized_dx = dx / distance
    normalized_dy = dy / distance

    return (normalized_dx, normalized_dy)

def ifReachedPath(x, y, path_x, path_y, motion_vector_x, motion_vector_y):
    if motion_vector_x < 0 and motion_vector_y < 0:
        if x <= path_x and y <= path_y:
            return True
    elif motion_vector_x >= 0 and motion_vector_y < 0:
        if x >= path_x and y <= path_y:
            return True
    elif motion_vector_x < 0 and motion_vector_y >= 0:
        if x <= path_x and y >= path_y:
            return True
    elif motion_vector_x >= 0 and motion_vector_y >= 0:
        if x >= path_x and y >= path_y:
            return True
        
    return False

def isCircleInsideCircle(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if (r1 + r2 > d and r1 + d > r2 and r2 + d > r1) or (r1 + d < r2):
        return True
    return False