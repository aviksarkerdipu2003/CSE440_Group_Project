import heapq
from collections import deque

from core.node import Node
from core.metrics import Metrics
from core.utils import make_hashable, reconstruct_path

def bfs(problem):
    m=Metrics(); m.start_timer()
    root=Node(problem.initial_state()); q=deque([root]); seen={make_hashable(root.state)}
    while q:
        n=q.popleft()
        if problem.goal_test(n.state):
            p=reconstruct_path(n); m.solution_length=len(p)-1; m.stop_timer(); return p,m.summary()
        m.nodes_expanded+=1; m.max_depth=max(m.max_depth,n.depth)
        for ns,c in problem.get_neighbors(n.state):
            k=make_hashable(ns)
            if k not in seen:
                seen.add(k); q.append(Node(ns,n,n.path_cost+c,n.depth+1))
    m.stop_timer(); return None,m.summary()

def dfs(problem):
    m=Metrics(); m.start_timer()
    root=Node(problem.initial_state()); stack=[root]; seen=set()
    while stack:
        n=stack.pop(); k=make_hashable(n.state)
        if k in seen: continue
        if problem.goal_test(n.state):
            p=reconstruct_path(n); m.solution_length=len(p)-1; m.stop_timer(); return p,m.summary()
        seen.add(k); m.nodes_expanded+=1; m.max_depth=max(m.max_depth,n.depth)
        for ns,c in reversed(problem.get_neighbors(n.state)):
            stack.append(Node(ns,n,n.path_cost+c,n.depth+1))
    m.stop_timer(); return None,m.summary()

def dls(problem,limit=20):
    m=Metrics(); m.start_timer()
    stack=[Node(problem.initial_state())]; seen=set()
    while stack:
        n=stack.pop()
        if problem.goal_test(n.state):
            p=reconstruct_path(n); m.solution_length=len(p)-1; m.stop_timer(); return p,m.summary()
        if n.depth>=limit: continue
        k=make_hashable(n.state)
        if k in seen: continue
        seen.add(k); m.nodes_expanded+=1; m.max_depth=max(m.max_depth,n.depth)
        for ns,c in reversed(problem.get_neighbors(n.state)):
            stack.append(Node(ns,n,n.path_cost+c,n.depth+1))
    m.stop_timer(); return None,m.summary()

def iddfs(problem,max_depth=30):
    last=None
    for d in range(max_depth+1):
        p,m=dls(problem,d); last=m
        if p: return p,m
    return None,last

def ucs(problem):
    m=Metrics(); m.start_timer()
    root=Node(problem.initial_state()); pq=[]; counter=0
    heapq.heappush(pq,(0,counter,root)); best={make_hashable(root.state):0}; done=set()
    while pq:
        cost,_,n=heapq.heappop(pq); k=make_hashable(n.state)
        if k in done: continue
        if problem.goal_test(n.state):
            p=reconstruct_path(n); m.solution_length=len(p)-1; m.stop_timer(); return p,m.summary()
        done.add(k); m.nodes_expanded+=1; m.max_depth=max(m.max_depth,n.depth)
        for ns,c in problem.get_neighbors(n.state):
            nk=make_hashable(ns); nc=cost+c
            if nk not in best or nc<best[nk]:
                best[nk]=nc; counter+=1; heapq.heappush(pq,(nc,counter,Node(ns,n,nc,n.depth+1)))
    m.stop_timer(); return None,m.summary()

def greedy(problem,h):
    m=Metrics(); m.start_timer()
    root=Node(problem.initial_state()); pq=[]; counter=0
    heapq.heappush(pq,(h(root.state),counter,root)); seen=set()
    while pq:
        _,_,n=heapq.heappop(pq); k=make_hashable(n.state)
        if k in seen: continue
        if problem.goal_test(n.state):
            p=reconstruct_path(n); m.solution_length=len(p)-1; m.stop_timer(); return p,m.summary()
        seen.add(k); m.nodes_expanded+=1; m.max_depth=max(m.max_depth,n.depth)
        for ns,c in problem.get_neighbors(n.state):
            counter+=1; heapq.heappush(pq,(h(ns),counter,Node(ns,n,n.path_cost+c,n.depth+1)))
    m.stop_timer(); return None,m.summary()

def astar(problem,h):
    m=Metrics(); m.start_timer()
    root=Node(problem.initial_state()); pq=[]; counter=0; best={make_hashable(root.state):0}; done=set()
    heapq.heappush(pq,(h(root.state),counter,root))
    while pq:
        _,_,n=heapq.heappop(pq); k=make_hashable(n.state)
        if k in done: continue
        if problem.goal_test(n.state):
            p=reconstruct_path(n); m.solution_length=len(p)-1; m.stop_timer(); return p,m.summary()
        done.add(k); m.nodes_expanded+=1; m.max_depth=max(m.max_depth,n.depth)
        for ns,c in problem.get_neighbors(n.state):
            nk=make_hashable(ns); ng=n.path_cost+c
            if nk not in best or ng<best[nk]:
                best[nk]=ng; counter+=1; heapq.heappush(pq,(ng+h(ns),counter,Node(ns,n,ng,n.depth+1)))
    m.stop_timer(); return None,m.summary()

def beam(problem,h,width=2):
    m=Metrics(); m.start_timer()
    frontier=[Node(problem.initial_state())]; seen=set()
    while frontier:
        nxt=[]
        for n in frontier:
            k=make_hashable(n.state)
            if k in seen: continue
            if problem.goal_test(n.state):
                p=reconstruct_path(n); m.solution_length=len(p)-1; m.stop_timer(); return p,m.summary()
            seen.add(k); m.nodes_expanded+=1; m.max_depth=max(m.max_depth,n.depth)
            for ns,c in problem.get_neighbors(n.state):
                nxt.append(Node(ns,n,n.path_cost+c,n.depth+1))
        nxt.sort(key=lambda x:h(x.state)); frontier=nxt[:width]
    m.stop_timer(); return None,m.summary()
