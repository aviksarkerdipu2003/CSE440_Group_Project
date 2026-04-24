from copy import deepcopy

class SudokuProblem:
    def __init__(self,start): self.start=start
    def initial_state(self): return self.start
    def valid_move(self,s,r,c,n):
        if any(s[r][j]==n for j in range(9) if j!=c): return False
        if any(s[i][c]==n for i in range(9) if i!=r): return False
        sr,sc=(r//3)*3,(c//3)*3
        for i in range(sr,sr+3):
            for j in range(sc,sc+3):
                if (i,j)!=(r,c) and s[i][j]==n: return False
        return True
    def goal_test(self,s):
        for r in range(9):
            for c in range(9):
                if s[r][c]==0 or not self.valid_move(s,r,c,s[r][c]): return False
        return True
    def find_empty(self,s):
        for r in range(9):
            for c in range(9):
                if s[r][c]==0: return r,c
        return None
    def get_neighbors(self,s):
        pos=self.find_empty(s)
        if pos is None: return []
        r,c=pos; out=[]
        for n in range(1,10):
            ns=deepcopy(s); ns[r][c]=n
            if self.valid_move(ns,r,c,n): out.append((ns,1))
        return out

def sudoku_h(s): return sum(1 for r in s for v in r if v==0)

def parse_sudoku(t):
    g=[[int(x) for x in line.replace(","," ").split()] for line in t.strip().splitlines() if line.strip()]
    if len(g)!=9 or any(len(r)!=9 for r in g): raise ValueError("Sudoku must be 9x9.")
    return g
