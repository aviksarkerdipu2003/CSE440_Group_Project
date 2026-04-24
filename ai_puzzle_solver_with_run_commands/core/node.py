class Node:
    def __init__(self,state,parent=None,path_cost=0,depth=0):
        self.state=state; self.parent=parent; self.path_cost=path_cost; self.depth=depth
    def __lt__(self,o): return self.path_cost < o.path_cost
