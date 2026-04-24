class MazeProblem:
    def __init__(self,grid,start,goal):
        self.grid=grid; self.rows=len(grid); self.cols=len(grid[0]); self.start=start; self.goal=goal
        self.valid(start); self.valid(goal)
    def valid(self,p):
        r,c=p
        if not(0<=r<self.rows and 0<=c<self.cols): raise ValueError(f"Invalid position {p}")
        if self.grid[r][c]==1: raise ValueError(f"Position {p} is blocked.")
    def initial_state(self): return self.start
    def goal_test(self,s): return s==self.goal
    def get_neighbors(self,s):
        r,c=s; out=[]
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<self.rows and 0<=nc<self.cols and self.grid[nr][nc]==0:
                out.append(((nr,nc),1))
        return out

def maze_manhattan(s,g): return abs(s[0]-g[0])+abs(s[1]-g[1])

def parse_maze(t):
    g=[[int(x) for x in line.replace(","," ").split()] for line in t.strip().splitlines() if line.strip()]
    if not g or any(len(r)!=len(g[0]) for r in g): raise ValueError("Invalid maze grid.")
    return g
