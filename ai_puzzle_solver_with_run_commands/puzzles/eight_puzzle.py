class EightPuzzleProblem:
    def __init__(self,start,goal=None):
        self.start=start; self.goal=goal or [1,2,3,4,5,6,7,8,0]
        self.validate(start); self.validate(self.goal)
    def validate(self,s):
        if not isinstance(s,list) or len(s)!=9 or sorted(s)!=list(range(9)):
            raise ValueError("8 Puzzle must contain digits 0 to 8 exactly once.")
    def initial_state(self): return self.start
    def goal_test(self,s): return s==self.goal
    def get_neighbors(self,s):
        z=s.index(0); r,c=z//3,z%3; out=[]
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<3 and 0<=nc<3:
                ni=nr*3+nc; ns=s[:]; ns[z],ns[ni]=ns[ni],ns[z]; out.append((ns,1))
        return out

def ep_manhattan(s,goal):
    gp={v:(i//3,i%3) for i,v in enumerate(goal)}
    return sum(abs(i//3-gp[v][0])+abs(i%3-gp[v][1]) for i,v in enumerate(s) if v!=0)

def parse_8(t):
    s=[int(x) for x in t.replace(","," ").split()]
    if len(s)!=9 or sorted(s)!=list(range(9)): raise ValueError("Enter digits 0 to 8 exactly once.")
    return s
