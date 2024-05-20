import math

def calculate_horizontal_length(start, end):
    """Calculate the horizontal length of a beam."""
    return abs(end[0] - start[0])

def calculate_vertical_length(start, end):
    """Calculate the vertical length of a beam."""
    return abs(end[1] - start[1])

def calculate_real_length(start, end):
    """Calculate the real length of a beam."""
    return math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)

def calculate_angle(start, end):
    """Calculate the angle of a beam in degrees."""
    return math.degrees(math.atan2(end[1] - start[1], end[0] - start[0]))
