def euclidean_distance(pos, goal):
    return ((pos[0]-goal[0])**2 + (pos[1]-goal[1])**2) ** 0.5

def manhattan_distance(pos, goal):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])