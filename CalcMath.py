import math

def normalized_xy(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    distance = math.sqrt(dx**2 + dy**2)

    normalized_dx = dx / distance
    normalized_dy = dy / distance

    return (normalized_dx, normalized_dy)

def ifReachedPath(current_coords, path, motion_vector):
    if motion_vector[0] < 0 and motion_vector[1] < 0:
        if current_coords[0] <= path[0] and current_coords[1] <= path[1]:
            return True
    elif motion_vector[0] >= 0 and motion_vector[1] < 0:
        if current_coords[0] >= path[0] and current_coords[1] <= path[1]:
            return True
    elif motion_vector[0] < 0 and motion_vector[1] >= 0:
        if current_coords[0] <= path[0] and current_coords[1] >= path[1]:
            return True
    elif motion_vector[0] >= 0 and motion_vector[1] >= 0:
        if current_coords[0] >= path[0] and current_coords[1] >= path[1]:
            return True
        
    return False