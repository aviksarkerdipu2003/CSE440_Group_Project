def make_hashable(s):
    if isinstance(s, list):
        if s and isinstance(s[0], list): return tuple(tuple(r) for r in s)
        return tuple(s)
    return s

def reconstruct_path(n):
    p=[]
    while n:
        p.append(n.state); n=n.parent
    return list(reversed(p))
