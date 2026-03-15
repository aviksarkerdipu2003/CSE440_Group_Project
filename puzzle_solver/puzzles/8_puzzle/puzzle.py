from core.problem import Problem

class EightPuzzle(Problem):
    def __init__(self, board):
        if not self.is_valid(board):
            raise ValueError("Invalid 8-puzzle configuration")
        self.board = board
        self.size = 3
        self.goal = [[1,2,3],[4,5,6],[7,8,0]]

    def is_valid(self, board):
        flat = [x for row in board for x in row if x != 0]
        inversions = sum(
            1 for i in range(len(flat)) for j in range(i+1, len(flat)) if flat[i] > flat[j]
        )
        return inversions % 2 == 0

    def initial_state(self):
        return self.board

    def goal_test(self, state):
        return state == self.goal

    def get_neighbors(self, state):
        neighbors = []
        x, y = [(ix, iy) for ix, row in enumerate(state) for iy, val in enumerate(row) if val == 0][0]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                neighbors.append(new_state)
        return neighbors

    def pretty_print(self, state):
        for row in state:
            print(" ".join(str(x) if x != 0 else "_" for x in row))
        print()
