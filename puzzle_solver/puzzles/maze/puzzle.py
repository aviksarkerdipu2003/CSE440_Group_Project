from core.problem import Problem

class Maze(Problem):
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        if not self.is_valid():
            raise ValueError("Invalid maze configuration")

    def is_valid(self):
        sx, sy = self.start
        gx, gy = self.goal
        return (
            0 <= sx < len(self.grid) and 0 <= sy < len(self.grid[0]) and
            0 <= gx < len(self.grid) and 0 <= gy < len(self.grid[0]) and
            self.grid[sx][sy] == 0 and self.grid[gx][gy] == 0
        )

    def initial_state(self):
        return self.start

    def goal_test(self, state):
        return state == self.goal

    def get_neighbors(self, pos):
        x, y = pos
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]) and self.grid[nx][ny] == 0:
                neighbors.append((nx, ny))
        return neighbors

    def pretty_print(self, state):
        print(f"Current position: {state}")
