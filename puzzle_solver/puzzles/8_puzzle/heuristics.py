def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == val:
                            distance += abs(i - x) + abs(j - y)
    return distance
